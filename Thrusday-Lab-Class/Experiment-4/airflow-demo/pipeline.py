from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import steps

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='ml_pipeline_airflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["mlops", "demo"]
) as dag:

    load_data = PythonOperator(
        task_id='load_data',
        python_callable=steps.save_iris_data,
    )

    preprocess = PythonOperator(
        task_id='preprocess',
        python_callable=steps.preprocess_data,
    )

    train = PythonOperator(
        task_id='train',
        python_callable=steps.train_model,
    )

    evaluate = PythonOperator(
        task_id='evaluate',
        python_callable=steps.evaluate_model,
    )

    load_data >> preprocess >> train >> evaluate
