from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.app import ingestion_handler, preparation_handler

# Define a DAG
with DAG(
    "teste",
    start_date=datetime(2023, 10, 10), 
    schedule_interval=timedelta(minutes=60),
    catchup=False
) as dag:

    # Task para o ingestion_handler
    t0 = PythonOperator(
        task_id='ingestion_task',
        python_callable=ingestion_handler,
        op_kwargs =  {"event": {"subsource": "coingecko"}} # Chamando a função diretamente
    )

    # Task para o preparation_handler
    t1 = PythonOperator(
        task_id='preparation_task',
        python_callable=preparation_handler,
        op_kwargs =  {"event": {"subsource": "coingecko"}}   # Chamando a função diretamente
    )

    # Definindo a sequência de execução
    t0 >> t1