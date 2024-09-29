export RAW_PATH=/app/AWS/S3/RAW/
export WORK_PATH=/app/AWS/S3/WORK/
export RAW_CONFIG=/app/config.ingestion.json
export WORK_CONFIG=/app/config.preparation.json
export UTILS_PATH=/app/assets
export APP_PATH=/app/src

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

all: venv venv_requirements venv_run