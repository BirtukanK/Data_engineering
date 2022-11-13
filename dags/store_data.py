from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta,datetime
import airflow
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    "owner": "birtukan",
    "retries": 1,
    "email": ["birtukankuma1113@gmail.com"],
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    dag_id="Store_data",
    start_date=datetime(2022,10,11),
    schedule_interval="0 0 * * *",
    catchup=False,
    default_args=default_args,
) as dag_script:
    

    create_table = PostgresOperator(
        task_id="Create_table",
        postgres_conn_id="traffic_id",
        dag=dag_script,
        sql="""create table if not exists traffic_data
        (id int primary key,
        track_id int not null,
        v_type varchar(120) NOT null,
        traveled_d varchar(120) NOT null,
        avg_speed float NOT null,
        lat float NOT null,
        lon float NOT null,
        speed float NOT null,
        lon_acc float NOT null,
        lat_acc float NOT null,
        d_time float NOT null);""",
            
    )
    add_data = PostgresOperator(
        sql="""create table if not exists traffic_data
(id int primary key,
track_id int not null,
v_type varchar(120) NOT null,
traveled_d varchar(120) NOT null,
avg_speed float NOT null,
lat float NOT null,
lon float NOT null,
speed float NOT null,
lon_acc float NOT null,
lat_acc float NOT null,
d_time float NOT null);""",
        task_id="Add_data",
        postgres_conn_id="traffic_id",
        dag=dag_script,
    )
    create_database = PostgresOperator(
        sql="sql/create_db.sql",
        task_id="Create_database",
        postgres_conn_id="traffic_id",
        dag=dag_script,
    )

create_table >> add_data >> create_database

if __name__ == '__main__ ':
    dag_script.cli()
