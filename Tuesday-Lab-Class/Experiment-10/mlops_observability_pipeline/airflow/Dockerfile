FROM apache/airflow:2.7.1-python3.9

USER airflow
RUN pip install prometheus_client

COPY ./dags /opt/airflow/dags

USER airflow
