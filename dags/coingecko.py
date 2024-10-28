from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from app import ingestion_handler, preparation_handler

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'coningecko',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    tarefa_ingestao = PythonOperator(
        task_id='ingestao',
        python_callable=ingestion_handler,
        op_kwargs={'subsource': 'coingecko'},
    )

    tarefa_preparacao = PythonOperator(
        task_id='preparacao',
        python_callable=preparation_handler,
        op_kwargs={'subsource': 'coingecko'},
    )

    tarefa_ingestao >> tarefa_preparacao  
