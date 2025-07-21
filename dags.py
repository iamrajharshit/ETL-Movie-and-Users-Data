import airflow
from airflow.models import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
from transformation import *

##define the etl function

def etl():
    movies_df = extract_movies_to_df()
    users_df = extract_users_to_df()
    transformed_df = transform_avg_ratings(movies_df, users_df)
    load_df_to_db(transformed_df)


# arg for DAG 
default_args = {
    'owner': 'harshit',
    'depends_on_past': True, #init False
    'start_date': datetime(2025, 7, 21),
    'email': ['harshit@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=30),
}


dag= DAG(dag_id="etl_pipeline",
         default_args=default_args,
         description="ETL pipeline for avg ratings",
         schedule_interval=timedelta(days=1),
         catchup=False,
         tags=['etl'],
         )

etl_task = PythonOperator(task_id="etl_task", python_callable=etl, dag=dag)

etl()

