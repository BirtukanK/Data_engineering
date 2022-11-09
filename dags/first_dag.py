from datetime import datetime, timedelta
import imp
from airflow import DAG
from airflow.decorators import task
from sqlalchemy import create_engine
import os
from airflow.operators.python import PythonOperator



with DAG(
    dag_id='First_DAG',
    # default_args=default_args,
    description='First DAG prepared',
    schedule_interval='@daily',
    start_date=datetime(2022,1,1),
    catchup=False,
    tags=['The first tag'],
)as dag:
    
     

    # specific tasks
    @task(task_id="first task")
    def performs_a_task():
        print("Data warehousing")
        return "Data warehousing"

    performs_a_task 

    @task(task_id='load')
    def load_data(file_path, db_table):
        engine = create_engine('postgesql+psycopg2://airflow:airflow@postgres/postgres_database')
        print(os.system('pwd'))
        df = pd.read_csv(file_path,sep="[,;:]",index_col=False)
        df.to_sql(db_table,con=engine,if_exists='replace',index_label='id')
    first_task = PythonOperator(
        task_id="load",
        python_callable=load_data,
        op_kwargs={
            "path": "./data/data_1.csv",
            "db_table": "traffic_data"
        }
    )
    first_task
    

    