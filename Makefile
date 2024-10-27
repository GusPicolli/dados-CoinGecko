export RAW_PATH = ../dados-CoinGecko/AWS/S3/RAW/
export WORK_PATH = ../dados-CoinGecko/AWS/S3/WORK/
export RAW_CONFIG = ./assets/config.ingestion.json
export WORK_CONFIG = ./assets/config.preparation.json
#export UTILS_PATH=../dados-CoinGecko/assets
#export APP_PATH=../dados-CoinGecko/src

export RAW_PATH_DOCKER=/app/AWS/S3/RAW/
export WORK_PATH_DOCKER=/app/AWS/S3/WORK/
export RAW_CONFIG_DOCKER=/app/assets/config.ingestion.json
export WORK_CONFIG_DOCKER=/app/assets/config.preparation.json

## VENV ##
venv:
	python -m venv venv 

venv_requirements:
	venv\Scripts\activate && pip install -r requirements.txt 

venv_run:
	venv\Scripts\activate && python src/app.py

## VENV TESTS ##
venv_requirements_tests:
	venv\Scripts\activate && pip install -r requirements-dev.txt 

venv_run_tests:
	venv\Scripts\activate && pytest tests/ingestion_preparation_test.py

## REMOVE VNV ##
venv_remove:
	rmdir /S /Q venv

## LOCAL ##
requirements:
	pip install -r requirements.txt

run: 
	python src/app.py

run_tests:
	pytest tests/ingestion_preparation_test.py

## DOCKER ##

docker_build:
	cd docker && docker-compose up --build

docker_run_ingestion:
	cd docker && docker-compose up ingestion

docker_run_preparation:
	cd docker && docker-compose up preparation
	
docker_run:
	cd docker && docker-compose up

## CPROFILE ##

cprofile_time:
	python -m cProfile -s time src/app.py

cprofile_perf:
	python -m cProfile -o file_profiling.prof src/app.py

## SNAKEVIZ ##

snakeviz:
	snakeviz file_profiling.prof
 
all: venv venv_requirements venv_run

