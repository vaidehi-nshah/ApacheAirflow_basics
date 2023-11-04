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
dag = DAG(dag_id='DAG-2', default_args=default_args, catchup=False, schedule_interval='@once')

# STEP: 4
### define tasks
A = DummyOperator(task_id='A', dag=dag)
B = DummyOperator(task_id='B', dag=dag)
C = DummyOperator(task_id='C', dag=dag)
D = DummyOperator(task_id='D', dag=dag)
E = DummyOperator(task_id='E', dag=dag)
F = DummyOperator(task_id='F', dag=dag)

# STEP: 5
### define dependencies
A >> B
B >> C
B >> D
C >> [E,F] 