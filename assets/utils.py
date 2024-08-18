from datetime import datetime
import requests,json
import pandas as pd
import pyarrow
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def ingestion(event: dict):
  config_ingestion = json.load(open('./assets/config.ingestion.json'))
  response = requests.get(config_ingestion["url"], params=config_ingestion["parameters"])
  data = response.json()
  df = pd.DataFrame(data)
  df.to_parquet('../dados-CoinGecko/AWS/S3/RAW/coins_list_raw.parquet')
  logger.info("arquivo salvo em RAW")

def preparation(event: dict):
  metadado = json.load(open('./assets/config.preparation.json'))
  dataframe = pd.read_parquet('../dados-CoinGecko/AWS/S3/RAW/coins_list_raw.parquet')

  for coluna in metadado:
    if metadado[coluna] == 'string':
      dataframe[coluna] = dataframe[coluna].astype(str)
    if metadado[coluna] == 'double':
      dataframe[coluna] = dataframe[coluna].astype(float)
    if metadado[coluna] == 'timestamp':
      dataframe[coluna] = pd.to_datetime(dataframe[coluna]).dt.strftime('%Y-%m-%d %H:%M:%S')
  
  dataframe.to_parquet(f'../dados-CoinGecko/AWS/S3/WORK/coins_list_work.parquet')
  logger.info("arquivo salvo em WORK")
