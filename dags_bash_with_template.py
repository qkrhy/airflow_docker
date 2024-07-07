from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    # 누락된 구간을 돌리지 않음
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo "data_interval_end: {{ data_interval_end }}  "'
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            # date_interval_start : 타임스탬프 +> | ds : 날짜 형식으로 변환
            'START_DATE':'{{data_interval_start | ds }}',
            'END_DATE':'{{data_interval_end | ds }}'
        },
         # && : 앞의 명령어가 성공했을 때 뒤의 명령어 실행
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2