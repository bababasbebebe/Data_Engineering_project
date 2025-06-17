from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
import pandas as pd
import numpy as np
import logging
import os

# Задается путь к файлу
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

# Настройка логгера
logger = logging.getLogger(__name__)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
    'email_on_retry': False,
}

# Таски для передачи аргументов между функциями.
def load_data_task(**kwargs):
    from etl.Load import load_data
    ti = kwargs['ti']

    features, target = load_data()

    # Сохраняем в XCom для передачи между функциями
    ti.xcom_push(key='features', value=features.to_json())
    ti.xcom_push(key='target', value=target.to_json())

    # Сохраняем артефакты в файлы
    features.to_csv(os.path.join(RESULTS_DIR, 'features.csv'), index=False)
    target.to_csv(os.path.join(RESULTS_DIR, 'target.csv'), index=False)


def preprocess_task(**kwargs):
    from etl.Preprocessing import preprocess
    ti = kwargs['ti']

    # Получаем данные из предыдущей функции
    features = pd.read_json(ti.xcom_pull(task_ids='load_data', key='features'))
    target = pd.read_json(ti.xcom_pull(task_ids='load_data', key='target'))

    # Выполняем предобработку
    X_train, X_test, y_train, y_test = preprocess(features, target)

    # Сохраняем результаты в XCom
    ti.xcom_push(key='X_train', value=X_train.tolist())
    ti.xcom_push(key='X_test', value=X_test.tolist())
    ti.xcom_push(key='y_train', value=y_train.values.tolist())
    ti.xcom_push(key='y_test', value=y_test.values.tolist())


def train_model_task(**kwargs):
    from etl.Training import train_model
    ti = kwargs['ti']

    # Получаем данные
    X_train = np.array(ti.xcom_pull(task_ids='preprocess_data', key='X_train'))
    y_train = np.array(ti.xcom_pull(task_ids='preprocess_data', key='y_train'))

    # Задаем имя модели через Variable или напрямую
    model_name = Variable.get("model_name", default_var="breast_cancer_model")
    model_path = os.path.join(RESULTS_DIR, model_name)

    # Обучаем модель
    saved_model_path = train_model(X_train, y_train, model_path)
    ti.xcom_push(key='model_path', value=saved_model_path)


def evaluate_model_task(**kwargs):
    from etl.Evaluation import evaluate
    ti = kwargs['ti']

    # Получаем данные
    X_test = np.array(ti.xcom_pull(task_ids='preprocess_data', key='X_test'))
    y_test = np.array(ti.xcom_pull(task_ids='preprocess_data', key='y_test'))
    model_path = ti.xcom_pull(task_ids='train_model', key='model_path')

    # Задаем имя для метрик
    metrics_name = Variable.get("metrics_name", default_var="model_metrics")
    metrics_path = os.path.join(RESULTS_DIR, metrics_name)

    # Оцениваем модель
    evaluate(X_test, y_test, model_path.replace('.pkl', ''), metrics_path)


with DAG(
        'breast_cancer_ml_pipeline',
        default_args=default_args,
        description='Полный пайплайн для классификации рака груди',
        schedule_interval='@daily',
        catchup=False,
        tags=['medical', 'ml'],
) as dag:
    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_data_task,
        provide_context=True,
    )

    preprocess_data = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_task,
        provide_context=True,
    )

    train_model = PythonOperator(
        task_id='train_model',
        python_callable=train_model_task,
        provide_context=True,
    )

    evaluate_model = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model_task,
        provide_context=True,
    )

    # Определяем порядок выполнения
    load_data >> preprocess_data >> train_model >> evaluate_model


    # Настройка обработки ошибок
    def task_failure_alert(context):
        logger.error(f"Task {context['task_instance'].task_id} failed")


    for task in dag.tasks:
        task.on_failure_callback = task_failure_alert
