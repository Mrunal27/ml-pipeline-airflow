from airflow import DAG
from airflow.operators.python import PythonOperator
from prepare_dataset import prepare
from datetime import datetime
import sys
import os

# Add your project root to sys.path so Airflow can find your scripts
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from prepare_dataset import prepare
from ml.train import train_model
from ml.evaluate import evaluate_model

default_args = {
    "owner": "mrunal",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="ml_pipeline_dag",
    default_args=default_args,
    schedule=None,  # Use 'schedule' instead of 'schedule_interval'
    catchup=False,
    tags=["ml", "pipeline"],
) as dag:

    prepare_task = PythonOperator(
        task_id="prepare_dataset",
        python_callable=prepare,
        op_args=["data/housing.csv"],
    )

    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
        op_args=["data/housing.csv", "ml/model.pkl"],
    )

    evaluate_task = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_model,
        op_args=["data/housing.csv", "ml/model.pkl"],
    )

    prepare_task >> train_task >> evaluate_task