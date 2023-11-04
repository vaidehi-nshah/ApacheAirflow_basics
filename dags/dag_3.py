# STEP: 1
### importing modules
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

# STEP: 2
### default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 28),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# STEP: 3
### instantiate DAG
dag = DAG(dag_id='DAG-3', default_args=default_args, catchup=False, schedule_interval=None)

# STEP: 4
### define tasks

# Task to be queued
queue_task = DummyOperator(task_id='queue_task', dag=dag)

# Task that fails
def fail_task():
    raise Exception("This task is designed to fail.")

fail_task = PythonOperator(
    task_id='fail_task',
    python_callable=fail_task,
    dag=dag,
)

# Task that succeeds
def run_task():
    print("This task is running successfully.")

run_task = PythonOperator(
    task_id='run_task',
    python_callable=run_task,
    dag=dag,
)

# Task that is skipped
skip_task = DummyOperator(task_id='skip_task', dag=dag, trigger_rule=TriggerRule.ONE_FAILED)

# STEP: 5
### define dependencies
queue_task >> fail_task
queue_task >> run_task
fail_task >> skip_task
run_task >> skip_task
