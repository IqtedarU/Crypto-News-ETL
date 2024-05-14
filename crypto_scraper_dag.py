from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import crypto_scraper 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'crypto_scraper_dag',
    default_args=default_args,
    description='Scrape cryptocurrency articles daily',
    schedule_interval=timedelta(days=1),
)

run_scraper = PythonOperator(
    task_id='run_scraper',
    python_callable=crypto_scraper.scrape_articles,
    dag=dag,
)

run_scraper
