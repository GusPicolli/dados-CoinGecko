export RAW_PATH = ../dados-CoinGecko/AWS/S3/RAW/
export WORK_PATH = ../dados-CoinGecko/AWS/S3/WORK/
export RAW_CONFIG = ./assets/config.ingestion.json
export WORK_CONFIG = ./assets/config.preparation.json
export UTILS_PATH=../dados-CoinGecko/assets
export APP_PATH=../dados-CoinGecko/src

export RAW_PATH_DOCKER=/app/AWS/S3/RAW/
export WORK_PATH_DOCKER=/app/AWS/S3/WORK/
export RAW_CONFIG_DOCKER=/app/config.ingestion.json
export WORK_CONFIG_DOCKER=/app/config.preparation.json

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

docker_build:
	cd docker && docker-compose up --build

docker_run:
	cd docker && docker-compose up

cprofile_time:
	set PYTHONPATH=${UTILS_PATH} && python -m cProfile -s time src/app.py

cprofile_perf:
	set PYTHONPATH=${UTILS_PATH} && python -m cProfile -o file_profiling.prof src/app.py

snakeviz:
	snakeviz file_profiling.prof

all: venv venv_requirements venv_run