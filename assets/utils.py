from datetime import datetime
import requests,json
import pandas as pd
import pyarrow

path_local = 'C:/Users/gusta/Desktop/'

def ingestion(event: dict):
  config_ingestion = json.load(open('./assets/config.ingestion.json'))
  response = requests.get(config_ingestion["url"], params=config_ingestion["parameters"])
  data = response.json()
  df = pd.DataFrame(data)
  df.to_parquet(f'{path_local}dados-CoinGecko/AWS/S3/RAW/coins_list_raw.parquet')
  print("arquivo salvo em RAW")

def preparation(event: dict):
  metadado = json.load(open('./assets/config.preparation.json'))
  dataframe = pd.read_parquet(f'{path_local}dados-CoinGecko/AWS/S3/RAW/coins_list.parquet')

  for coluna in metadado:
    if metadado[coluna] == 'string':
      dataframe[coluna] = dataframe[coluna].astype(str)
    if metadado == 'double':
      dataframe[coluna] = dataframe[coluna].astype(float)
    if metadado == 'timestamp':
      dataframe[coluna] = datetime.strptime(dataframe[coluna], formato = "%Y-%m-%d %H:%M:%S")
  
  dataframe.to_parquet(f'{path_local}dados-CoinGecko/AWS/S3/WORK/coins_list_work.parquet')
  print("arquivo salvo em WORK")
