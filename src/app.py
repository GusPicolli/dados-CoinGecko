import requests
import json
import datetime as dt
import utils
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def ingestion_handler(event: dict) -> dict:
    """
    Handles data ingestion.

    Logs the start and end times, and calls the 'ingestion' function from 'utils'.
    
    Args:
        event (dict): A dictionary with the parameters for ingestion. Example:
            {
                "subsource": "coingecko"
            }
    
    Returns:
        dict: The result from the 'ingestion' function.
    """
    logger.info("Início da ingestão: %s", str(dt.datetime.now()))
    payload = utils.ingestion(event)
    logger.info("Fim da ingestão: %s", str(dt.datetime.now()))
    return payload


def preparation_handler(event: dict) -> dict:
    """
    Handles data preparation.

    Logs the start and end times, and calls the 'preparation' function from 'utils'.
    
    Args:
        event (dict): A dictionary with the parameters for preparation. Example:
            {
                "subsource": "coingecko",
                "path": "./AWS/S3/RAW"
            }
    
    Returns:
        dict: The result from the 'preparation' function.
    """
    logger.info("Início da preparação: %s", str(dt.datetime.now()))
    payload = utils.preparation(event)
    logger.info("Fim da preparação: %s", str(dt.datetime.now()))
    return payload


if __name__ == "__main__":
    ingestion_handler({
        "subsource": "coingecko"
    })
    preparation_handler({
        "subsource": "coingecko"
    })