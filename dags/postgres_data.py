from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta,datetime
import airflow
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG(
    dag_id="dag_postgres",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@once",
    catchup=False,
) as dag:
    

    get_all_traffic= PostgresOperator(
        task_id="dag_postgres", 
        postgres_conn_id="postgres_traffic",
        sql="SELECT * FROM traffic_info;"
    )

    get_all_traffic 
