import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_traffic_data",
    schedule_interval='*/5 * * * *',
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    bash_t1 = BashOperator(
        task_id="rtm",
        bash_command="/opt/airflow/plugins/shell/start_traffic.sh rtm",
    )
    
    bash_t2 = BashOperator(
        task_id="rtti",
        bash_command="/opt/airflow/plugins/shell/start_traffic.sh rtti",
    )
    
    bash_t3 = BashOperator(
        task_id="pattern",
        bash_command="/opt/airflow/plugins/shell/start_traffic.sh pattern",
    )
    
    # bash_t1 -> bash_t2 순서로 실행
    bash_t1 >> bash_t2 >> bash_t3