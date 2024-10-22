FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ../assets /app
COPY ../src /app

ENV RAW_PATH_DOCKER=/app/AWS/S3/RAW/
ENV WORK_PATH_DOCKER=/app/AWS/S3/WORK/
ENV RAW_CONFIG_DOCKER=/app/config.ingestion.json
ENV WORK_CONFIG_DOCKER=/app/config.preparation.json

RUN mkdir -p /app/AWS/S3/RAW /app/AWS/S3/WORK

CMD ["python", "app.py"]