from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime

def start_learning():
    from train_model import main
    main()

dag = DAG('ml_pipeline',
          start_date=datetime(2024,1,1),
          schedule="* * * * *")

pull_task = BashOperator(task_id='pull_dvc', bash_command='dvc pull', dag=dag)
data_task = BashOperator(task_id='load_data', bash_command='python dataloader.py', dag=dag)
train_task = PythonOperator(task_id='train_model', python_callable=start_learning, dag=dag)
push_task = BashOperator(task_id='push_dvc', bash_command='dvc push', dag=dag)

pull_task >> data_task >> train_task >> push_task