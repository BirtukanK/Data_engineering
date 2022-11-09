from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta,datetime
import airflow
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG(
    dag_id="Store_data",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@once",
    catchup=False,
) as dag:
    

    create_table = PostgresOperator(
        sql="create_table.sql",
        task_id="Create_table",
        postgres_conn_id="postgres_default",
        dag=dag,
    )
    add_data = PostgresOperator(
        sql="add_data.sql",
        task_id="Add_data",
        postgres_conn_id="postgres_default",
        dag=dag,
    )
    create_databasse = PostgresOperator(
        sql="create_db.sql",
        task_id="Create_database",
        postgres_conn_id="postgres_default",
        dag=dag,
    )

create_table >> add_data >> create_databasse
