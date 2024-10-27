# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt .
RUN pip install -r requirements.txt

COPY ../assets /app
COPY ../src /app

ENV RAW_PATH=${RAW_PATH}
ENV WORK_PATH=${WORK_PATH}
ENV RAW_CONFIG=${RAW_CONFIG}
ENV WORK_CONFIG=${WORK_CONFIG}

# Defina um valor padrão para a variável FUNCTION
ENV FUNCTION="ingestion"

RUN mkdir -p /app/AWS/S3/RAW /app/AWS/S3/WORK

# Usar a variável FUNCTION para definir o comando a ser executado
CMD ["sh", "-c", "python src/app.py ${FUNCTION}"]