from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    # Dag의 이름 (Dag ID와 python 파일명을 동일하게) 
    dag_id="dags_bash_operator",
    # 분, 시 , 월, 요일, 언제 
    schedule="0 0 * * *",
    # dag가 시작되는 시간 (UTC 말고 한국시간) , 누락된 구간을 돌리지 않음 (catchup=False)
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    # 타임아웃 설정
    # dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    # [START howto_operator_bash]
    # task 객체명 : bash_t1 # 객체명과 task_id는 동일하게
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    
    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    
    # bash_t1 -> bash_t2 순서로 실행
    bash_t1 >> bash_t2