import airflow
from datetime import timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago

args = {'owner': 'airflow'}

default_args = {
    'owner': 'airflow',    
    #'start_date': airflow.utils.dates.days_ago(2),
    #'end_date': datetime(),
    #'depends_on_past': False,
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 5),
}

# SQL instruction to create the table
sql_create_table = """CREATE TABLE IF NOT EXISTS dsalabdw.tb_workers (id INT NOT NULL, name VARCHAR(250) NOT NULL, sector VARCHAR(250) NOT NULL);"""

# SQL instruction to insert data into the table
sql_insert_data = """
insert into dsalabdw.tb_workers (id, name, sector) values (1000, 'Bob', 'Marketing'), (1001, 'Maria', 'Accounting'),(1002, 'Jeremias', 'Data Engineering'), (1003, 'Messi', 'Marketing') ;"""


with DAG(dag_id = "lab5",
                   default_args = args,
                   # schedule_interval='0 0 * * *',
                   schedule_interval = '@once',  
                   dagrun_timeout = timedelta(minutes = 60),
                   description = 'ETL Job to create a table and insert data into it',
                   start_date = airflow.utils.dates.days_ago(1)) as dag:
    
    # Task to create the table
    create_table = PostgresOperator(sql = sql_create_table,
                               task_id = "create_table",
                               postgres_conn_id = "lab5_dw",
    )
    # task to insert data into the table
    insert_data = PostgresOperator(sql = sql_insert_data,
                                task_id = "insert_data",
                                postgres_conn_id = "lab5_dw",
    )
    # Dag execution flow
    create_table >> insert_data
