from datetime import datetime
import requests,json
import pandas as pd
import pyarrow
import os
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def ingestion(event: dict):
  config_ingestion = json.load(open('./assets/config.ingestion.json'))
  
  response = requests.get(config_ingestion["url"], params=config_ingestion["parameters"])
  data = response.json()
  
  df = pd.DataFrame(data)
  
  path_raw = os.getenv("RAW_PATH")
  df.to_parquet(f'{path_raw}coins_list_raw.parquet')
  
  logger.info("arquivo salvo em RAW")

def preparation(event: dict):
  metadado = json.load(open('./assets/config.preparation.json'))
  path_raw = os.getenv("RAW_PATH")
  dataframe = pd.read_parquet(path_raw)

  for coluna in metadado:
    if metadado[coluna] == 'string':
      dataframe[coluna] = dataframe[coluna].astype(str)
    if metadado[coluna] == 'double':
      dataframe[coluna] = dataframe[coluna].astype(float)
    if metadado[coluna] == 'timestamp':
      dataframe[coluna] = pd.to_datetime(dataframe[coluna]).dt.strftime('%Y-%m-%d %H:%M:%S')
  
  path_work = os.getenv("WORK_PATH")
  dataframe.to_parquet(f'{path_work}coins_list_work.parquet')
  logger.info("arquivo salvo em WORK")
