export RAW_PATH = ../dados-CoinGecko/AWS/S3/RAW/
export WORK_PATH = ../dados-CoinGecko/AWS/S3/WORK/
export RAW_CONFIG = ./assets/config.ingestion.json
export WORK_CONFIG = ./assets/config.preparation.json
export UTILS_PATH = ../dados-CoinGecko/assets
export APP_PATH = ../dados-CoinGecko/src

venv:
	python -m venv venv 

venv_requirements:
	venv\Scripts\activate && pip install -r requirements.txt 

venv_run:
	venv\Scripts\activate && set PYTHONPATH=${UTILS_PATH} && python src/app.py

venv_remove:
	rmdir /S /Q venv

requirements:
	pip install -r requirements.txt

run: 
	set PYTHONPATH=${UTILS_PATH} && python src/app.py

run_tests:
	set PYTHONPATH=${APP_PATH};${UTILS_PATH} && pytest tests/ingestion_preparation_test.py

all: venv venv_requirements venv_run