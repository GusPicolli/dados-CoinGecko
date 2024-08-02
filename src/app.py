import requests,json
import datetime as dt

def ingestion(event: dict):
  #faz a ingestao
  print("começo da ingestao as " + str(dt.datetime.now()))
  payload = event
  print("acabou a ingestao as " + str(dt.datetime.now()))
  return payload

if __name__ == "__main__":
  t = ingestion({
    "subsource": "coingecko"
    })
  print("Hello, World!" + str(t))