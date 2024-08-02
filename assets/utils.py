from datetime import datetime
import requests,json
import pandas as pd

def ingestion(event):
  config_ingestion = json.load(open('./assets/config.ingestion.json'))
  response = requests.get(config_ingestion["url"], params=config_ingestion["parametros"])
  data = response.json()
  df = pd.DataFrame(data)
  return df.to_parquet()

def preparation(dataframe):
  metadado = json.load(open('./assets/config.preparation.json'))
  for coluna in metadado:
    if metadado[coluna] == 'string':
      dataframe[coluna] = dataframe[coluna].astype(str)
    if metadado == 'double':
      dataframe[coluna] = dataframe[coluna].astype(float)
    if metadado == 'timestamp':
      dataframe[coluna] = datetime.strptime(dataframe[coluna], formato = "%Y-%m-%d %H:%M:%S")
  return dataframe
