import os
import json
import pytest
import pandas as pd
from app import ingestion_handler, preparation_handler


def test_ingestion():
    """
    Tests the ingestion function to ensure that:
    1. The function executes without errors.
    2. A parquet file is saved in the correct path.
    3. The saved file can be loaded as a DataFrame.

    The test fails if the ingestion function raises an exception, if the file is not found,
    or if the saved file is not of the correct type (parquet).
    """
    event = {"subsource": "coingecko"}

    try:
        ingestion_handler(event)
    except Exception as e:
        pytest.fail(f"Falha na função ingestion: {e}")

    arquivo_raw = os.path.join(os.getenv("RAW_PATH"), f"{event['subsource']}.parquet")
    assert os.path.exists(arquivo_raw), "Arquivo de saída não foi encontrado."

    try:
        df = pd.read_parquet(arquivo_raw)
        assert isinstance(df, pd.DataFrame), "O arquivo salvo não é um DataFrame."
    except Exception as e:
        pytest.fail(f"Erro ao ler o arquivo parquet: {e}")


def test_preparation():
    """
    Tests the preparation function to ensure that:
    1. The function executes without errors.
    2. The generated DataFrame has the correct columns according to the metadata.
    
    The test fails if the preparation function raises an exception, if the input file is not found,
    or if the generated DataFrame does not contain the expected columns.
    """
    event = {
        "subsource": "coingecko"
    }

    try:
        preparation_handler(event)
    except Exception as e:
        pytest.fail(f"Falha na função preparation: {e}")

    arquivo_work = os.path.join(os.getenv("WORK_PATH"), f"{event['subsource']}.parquet")
    assert os.path.exists(arquivo_work), "Arquivo de saída não foi encontrado."

    try:
        df = pd.read_parquet(arquivo_work)
    except Exception as e:
        pytest.fail(f"Erro ao ler o arquivo parquet: {e}")

    with open(os.getenv("WORK_CONFIG"), 'r') as config_file:
        metadado = json.load(config_file)

    colunas_metadado = set(metadado.keys())
    colunas_df = set(df.columns)
    assert colunas_metadado.issubset(colunas_df), "O DataFrame gerado não contém todas as colunas esperadas."
