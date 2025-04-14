from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from metrics_server import TASK_EXECUTIONS, start_metrics_server

start_metrics_server()  # Starts Prometheus server on port 8793

default_args = {
    'start_date': datetime(2024, 1, 1),
}

def preprocess_task():
    TASK_EXECUTIONS.labels(task_name="preprocess").inc()
    print("Preprocessing data...")

def train_task():
    TASK_EXECUTIONS.labels(task_name="train_model").inc()
    print("Training model...")

def evaluate_task():
    TASK_EXECUTIONS.labels(task_name="evaluate").inc()
    print("Evaluating model...")

with DAG('ml_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    preprocess = PythonOperator(
        task_id='preprocess',
        python_callable=preprocess_task
    )

    train = PythonOperator(
        task_id='train_model',
        python_callable=train_task
    )

    evaluate = PythonOperator(
        task_id='evaluate',
        python_callable=evaluate_task
    )

    preprocess >> train >> evaluate
