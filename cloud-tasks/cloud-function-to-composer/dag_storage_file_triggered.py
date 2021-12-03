import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag = DAG(
    'dag_storage_file_triggered',
    schedule_interval=None,
    start_date = datetime.now()
)

def print_file(**kwargs):
    logging.info(kwargs)

print_file_name = PythonOperator(
    dag = dag,
    task_id='print_file_name',
    python_callable=print_file,
    provide_context=True
)