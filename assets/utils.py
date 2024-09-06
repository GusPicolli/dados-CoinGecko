from datetime import datetime
import requests
import json
import pandas as pd
import pyarrow
import os
import logging
import env

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def request_data(url: str, params:dict) -> dict:
    """
    Sends a GET request to the specified URL with given parameters, returns the response as a dictionary.
        
        Args:
            url (str): The URL to send the request to.
            params (dict): The parameters to include in the request.
        
        Returns:
            dict: JSON response from the API.

        Raises:
            RequestException: If there's an issue with the HTTP request.
            JSONDecodeError: If the response cannot be parsed as JSON.
            Exception: For any unexpected errors.
    """
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
    """
    Saves the DataFrame as a Parquet file to the specified path.
        
        Args:
            df (pd.DataFrame): The data to be saved.
            path (str): Directory to save the file.
            filename (str): Name of the file.
        
        Returns:
            str: Path where the file was saved.

        Raises:
            KeyError: If a key is not found in the DataFrame.
            ValueError: If the data cannot be converted to a DataFrame.
            Exception: For any unexpected errors.
    """
    try:
        df.to_parquet(f'{path}{filename}.parquet')
        logger.info(f"Arquivo salvo em {path}{filename}")
    except KeyError as e:
        logger.error(f"Chave não encontrada no DataFrame: {e}")
        raise
    except ValueError as e:
        logger.error(f"Erro ao converter os dados para DataFrame: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado ao salvar o arquivo: {e}")
        raise

def ingestion(event: dict):
    """   
    Handles the ingestion process: requests data from a URL and saves it as a Parquet file.
        
        Args:
            event (dict): A dictionary with the event parameters, including the "subsource".
    """
    path_config = env.RAW_CONFIG
    config_ingestion = json.load(open(path_config))
  
    data = request_data(config_ingestion["url"], params=config_ingestion["parameters"])
    df = pd.DataFrame(data)

    path_raw = env.RAW_PATH
    load_data(df, path_raw, event["subsource"])

def preparation(event: dict):
    """
    Handles the preparation process: reads a Parquet file, transforms data types according to metadata, 
        and saves the processed data.
        
        Args:
            event (dict): A dictionary with the event parameters, including the "subsource".
    """
    path_config = env.WORK_CONFIG
    metadado = json.load(open(path_config))

    path_raw = env.RAW_PATH
    df = pd.read_parquet(path_raw)

    for coluna in metadado:
        try:
            if metadado[coluna] == 'string':
                df[coluna] = df[coluna].astype(str)
            if metadado[coluna] == 'double':
                df[coluna] = df[coluna].astype(float)
            if metadado[coluna] == 'timestamp':
                df[coluna] = pd.to_datetime(df[coluna]).dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            raise (f"Erro inesperado ao fazer a tratamento dos dados:{e}")
    
    path_work = env.WORK_PATH
    load_data(df, path_work, event["subsource"])
