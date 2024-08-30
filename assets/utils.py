from datetime import datetime
import requests
import json
import pandas as pd
import pyarrow
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def request_data(url: str, params:dict) -> dict:
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Erro ao fazer a requisição: {e}")
        raise
    except json.JSONDecodeError:
        logger.error("Erro ao decodificar a resposta JSON.")
        raise
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        raise

def load_data(df:pd.DataFrame, path: str, filename: str) -> str:
    try:
        df.to_parquet(f'{path}{filename}')
        logger.info(f"Arquivo salvo em {path}{filename}")
    except KeyError as e:
        logger.error(f"Chave não encontrada no DataFrame: {e}")
        raise
    except ValueError as e:
        logger.error("Erro ao converter os dados para DataFrame: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar o arquivo: {e}")
        raise

def ingestion(event: dict):
    
    path_config = os.getenv("RAW_CONFIG")
    config_ingestion = json.load(open(path_config))
  
    data = request_data(config_ingestion["url"], params=config_ingestion["parameters"])
    df = pd.DataFrame(data)

    path_raw = os.getenv("RAW_PATH")
    load_data(df, path_raw, event["subsource"])

def preparation(event: dict):

    path_config = os.getenv("WORK_CONFIG")
    metadado = json.load(open(path_config))

    path_raw = os.getenv("RAW_PATH")
    df = pd.read_parquet(path_raw)

    for coluna in metadado:
        if metadado[coluna] == 'string':
            df[coluna] = df[coluna].astype(str)
        if metadado[coluna] == 'double':
            df[coluna] = df[coluna].astype(float)
        if metadado[coluna] == 'timestamp':
            df[coluna] = pd.to_datetime(df[coluna]).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    path_work = os.getenv("WORK_PATH")
    load_data(df, path_work, event["subsource"])
