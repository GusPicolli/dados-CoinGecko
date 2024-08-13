import requests
import json
import datetime as dt
import sys
sys.path.insert(1, 'C:/Users/gusta/Desktop/dados-CoinGecko/assets')
import utils #import ingestion,preparation

def ingestion_handler(event: dict):
  #faz a ingestao
  print("começo da ingestao as " + str(dt.datetime.now()))
  payload = utils.ingestion(event)
  print("acabou a ingestao as " + str(dt.datetime.now()))
  return payload

def preparation_handler(event: dict):
  #faz a preparation
  print("começo da preparation as " + str(dt.datetime.now()))
  payload = utils.preparation(event)
  print("acabou a preparation as " + str(dt.datetime.now()))
  return payload

if __name__ == "__main__":
  ingestion_handler({
    "subsource": "coingecko"
    })
  preparation_handler({
    "subsource": "coingecko",
    "path": "./AWS/S3/RAW"
    })