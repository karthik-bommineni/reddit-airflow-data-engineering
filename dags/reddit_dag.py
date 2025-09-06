import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append("C://Users//karth//OneDrive//Desktop//DATA-ENGINEER-PROJECTS//reddit-airflow//")



from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'Karthik Bommineni',
    'start_date': datetime(2025, 8, 24)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
) 

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    do_xcom_push=True, # Pushing the CSV file into XCom
    dag = dag
)

# Upload to S3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3 # Executing the Task in order