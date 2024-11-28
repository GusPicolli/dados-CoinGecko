# Dockerfile
FROM apache/airflow:2.2.4-python3.9

WORKDIR /app

COPY ../requirements.txt .
RUN pip install -r requirements.txt

COPY ../assets /app
COPY ../src /app

ENV RAW_PATH=${RAW_PATH}
ENV WORK_PATH=${WORK_PATH}
ENV RAW_CONFIG=${RAW_CONFIG}
ENV WORK_CONFIG=${WORK_CONFIG}

RUN mkdir -p /app/AWS/S3/RAW /app/AWS/S3/WORK

CMD ["python", "app.py"]