# STEP: 1
### importing modules
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator  

# STEP: 2
### default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 28),
    'retries': 0
}

# STEP: 3
### instantiate DAG
dag = DAG(dag_id='DAG-1', default_args=default_args, catchup=False, schedule_interval='@once')

# STEP: 4
### define tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# STEP: 5
### define dependencies
start >> end
