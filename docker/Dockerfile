FROM python:3.11-slim

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY ../assets /app
COPY ../src /app

RUN mkdir -p /app/AWS/S3/RAW /app/AWS/S3/WORK

CMD ["python", "app.py"]