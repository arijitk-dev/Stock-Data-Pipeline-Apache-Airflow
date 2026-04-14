from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from extract import extract_data
from transform import transform_data
from analyze import analyze_data
from export import export_results


# ✅ Input file
DATA_FILE = "/Users/professorx/Documents/PythonUpgrad/C8_ApacheAirflow/assessment/data/Mastercard_stock.csv"

# ✅ Output files (IMPORTANT: file paths, not folders)
RAW_DATA = "/Users/professorx/Documents/PythonUpgrad/C8_ApacheAirflow/assessment/data/raw.csv"
CLEAN_DATA = "/Users/professorx/Documents/PythonUpgrad/C8_ApacheAirflow/assessment/data/clean.csv"
RESULT_FILE = "/Users/professorx/Documents/PythonUpgrad/C8_ApacheAirflow/assessment/data/result.csv"
RESULT_DIR = "/Users/professorx/Documents/PythonUpgrad/C8_ApacheAirflow/assessment/data/results"


with DAG(
    dag_id='stock_pipeline_final',
    start_date=datetime(2025, 1, 1),
    schedule='@weekly',
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        op_kwargs={
            'input_path': DATA_FILE,
            'output_path': RAW_DATA,
            'window_size': 100
        }
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_kwargs={
            'input_path': RAW_DATA,
            'output_path': CLEAN_DATA
        }
    )

    task_analyze = PythonOperator(
        task_id='analyze_data',
        python_callable=analyze_data,
        op_kwargs={
            'input_path': CLEAN_DATA,
            'output_path': RESULT_FILE
        }
    )

    task_export = PythonOperator(
        task_id='export_results',
        python_callable=export_results,
        op_kwargs={
            'input_path': CLEAN_DATA,
            'output_dir': RESULT_DIR
        }
    )

    # ✅ MUST be inside DAG block
    task_extract >> task_transform >> task_analyze >> task_export