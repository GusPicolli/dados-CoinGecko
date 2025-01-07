# Dockerfile
FROM apache/airflow:2.2.4-python3.9

ADD requirements.txt .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt

WORKDIR /opt/airflow/

ENV RAW_PATH=${RAW_PATH}
ENV WORK_PATH=${WORK_PATH}
ENV RAW_CONFIG=${RAW_CONFIG}
ENV WORK_CONFIG=${WORK_CONFIG}
ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/dags/src"

