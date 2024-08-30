import requests
import json
import datetime as dt
import sys
sys.path.insert(1, '../dados-CoinGecko/assets')
import utils 
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def ingestion_handler(event: dict):
  
  logger.info("Início da ingestao: " + str(dt.datetime.now()))
  payload = utils.ingestion(event)
  logger.info("Fim da ingestao: " + str(dt.datetime.now()))
  return payload

def preparation_handler(event: dict):
  
  logger.info("Início da preparacao: " + str(dt.datetime.now()))
  payload = utils.preparation(event)
  logger.info("Fim da preparacao: " + str(dt.datetime.now()))
  return payload

if __name__ == "__main__":
  ingestion_handler({
    "subsource": "coingecko"
    })
  preparation_handler({
    "subsource": "coingecko",
    "path": "./AWS/S3/RAW"
    })