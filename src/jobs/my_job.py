from dagster import job, op
import subprocess

@op
def run_ingest_script():
    # Replace the path with the actual location of ingest.py
    subprocess.run(['python', 'C:/Users/Sakshi/OneDrive/Desktop/ins-stock-analysis/notebooks/ins_ingest.py'], check=True)

@job
def my_job():
    run_ingest_script()
