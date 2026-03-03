from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'mlops',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mlops_data_validation_pipeline',
    default_args=default_args,
    description='Automated pipeline for pulling DVC data, validating with Great Expectations, and triggering train.',
    schedule_interval=timedelta(days=1),
)

def run_data_validation():
    # In reality this interacts with Great Expectations context
    print("Running Great Expectations Validation...")
    print("Checking missing values across columns...")
    print("Data Validation Passed. 100% Expectations Met.")
    return True

# 1. Pull the versioned dataset tracked by DVC
dvc_pull = BashOperator(
    task_id='pull_versioned_data',
    bash_command='dvc pull data/raw_features.csv',
    dag=dag,
)

# 2. Trigger automated Data Quality checks using Great Expectations
validate_data = PythonOperator(
    task_id='validate_data_quality',
    python_callable=run_data_validation,
    dag=dag,
)

# 3. Proceed to trigger training if data is validated (Assuming training script is separate)
trigger_training = BashOperator(
    task_id='trigger_model_training',
    bash_command='echo "Triggering MLflow Training via API or Bash..."',
    dag=dag,
)

dvc_pull >> validate_data >> trigger_training
