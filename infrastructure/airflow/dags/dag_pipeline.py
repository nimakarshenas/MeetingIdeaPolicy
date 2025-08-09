from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest_task():
    print("Stub: ingest audio/transcripts")

def promotion_task():
    print("Stub: light screening & promotion")

def nlp_task():
    print("Stub: full NLP on Tier‑A")

def gnn_task():
    print("Stub: nightly GNN jobs")

with DAG('gov_convo_intel_pipeline', start_date=datetime(2025,1,1), schedule='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='ingest', python_callable=ingest_task)
    t2 = PythonOperator(task_id='promote', python_callable=promotion_task)
    t3 = PythonOperator(task_id='nlp', python_callable=nlp_task)
    t4 = PythonOperator(task_id='gnn', python_callable=gnn_task)
    t1 >> t2 >> t3 >> t4
