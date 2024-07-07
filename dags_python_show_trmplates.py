from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    # 20240701 ~ 현재 날짜까지 실행
    start_date=pendulum.datetime(2024, 7, 1, tz="Asia/Seoul"),
    catchup=True
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint 
        pprint(kwargs)

    show_templates()