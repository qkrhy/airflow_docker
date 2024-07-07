from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    # 매월 1일 08시 실행
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        # 받는 사람 + 참조
        to='hyo8545@naver.com',
        # 이메일 제목 
        subject='Airflow 성공메일',
        html_content='Airflow 작업이 완료되었습니다'
    )