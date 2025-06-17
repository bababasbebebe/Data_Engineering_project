# Data_Engineering_project
*Работа выполнялась на виртуальной машине Linux Ubuntu. Airflow запускался через UI вебсервера, файлы логов и результатов пайплайна сохранялись на локальном диске.*

## 0. Логика репозитория
- [**dags/**](./dags/):
  - [main.py](./dags/main.py) с оркестрацией пайплайна.
  - [etl/](./dags/etl) с файлами ETL-компонентов:
    - [Load.py](./dags/etl/Load.py) с функцией загрузки.
    - [Preprocessing.py](./dags/etl/Preprocessing.py) с функцией предобработки данных и разбития на выборки.
    - [Training.py](./dags/etl/Training.py) с функцией обучения и сохранения модели.
    - [Evaluation.py](./dags/etl/Evaluation.py) с функцией тестирования модели, вычисления и сохранения метрик.
- [**logs/**](./logs/):
  - [dag_id=breast_cancer_ml_pipeline/](./logs/dag_id=breast_cancer_ml_pipeline/) с сохранением логов на каждом этапе ETL:
    - [task_id=load_data/](./logs/dag_id=breast_cancer_ml_pipeline/run_id=scheduled__2025-06-15T00_00_00+00_00/task_id=load_data/) - логи при загрузки данных.
    - [task_id=preprocess_data/](./logs/dag_id=breast_cancer_ml_pipeline/run_id=scheduled__2025-06-15T00_00_00+00_00/task_id=preprocess_data/) - логи при предобработке данных.
    - [task_id=train_model/](./logs/dag_id=breast_cancer_ml_pipeline/run_id=scheduled__2025-06-15T00_00_00+00_00/task_id=train_model/) - логи при обучении и сохранении модели.
    - [task_id=evaluate_model/](./logs/dag_id=breast_cancer_ml_pipeline/run_id=scheduled__2025-06-15T00_00_00+00_00/task_id=evaluate_model/) - логи при тестировании модели и подсчете метрик.
  - [scheduler/](./logs/scheduler/) с сохранением логов scheduler:
    - [2025-06-17/scheduler/](./logs/scheduler/2025-06-17/main.py.log) - сохранение логов файла с оркестрацией пайплайна.
- [**results/**](./results/):
  - [breast_cancer_model.pkl](./results/breast_cancer_model.pkl) - сохраненная модель.
  - [features.csv](./results/features.csv) - сохраненные при загрузки признаки датасета.
  - [target.csv](./results/target.csv) - сохраненная при загрузке целевая переменная датасета.
  - [model_metrics.json](./results/model_metrics.json) - сохраненные метрики.
  - [features_info.csv](./results/features_info.csv) - .info признаков.
  - [features_describe.csv](./results/features_describe.csv) - .describe признаков.
  - [figure.pdf](./results/figure.pdf) - распределение целевой переменной.
- [webserver_config.py](./webserver_config.py) - файл конфигурации вебсервера airflow.
- [requirements.txt](./requirements.txt).
      
## 1. Планирование пайплайна.
Решается задача бинарной классификации наличия рака груди.

### Описание датасета.
*[Датасет](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) числовых характеристик, полученных со снимка груди, для классификации наличия рака груди. Описательные харакетристики в [features_info.csv](./results/features_info.csv), [features_describe.csv](./results/features_describe.csv), [figure.pdf](./results/figure.pdf) файлах.*
- Датасет размером 569x30. Целевой переменной является target с бинарным значением наличия рака груди.
- Наличие рака в целевой переменной распределно в соотношении 2 к 1.
- Признаки имеют тип данных float64.
  
### Описание структуры пайплайна.
- Структура пайплана состоит из 4-х ETL компонентов:
  - Загрузка данных, сохранение описательных харакетристик датасета и сохранение признаков и целевой переменной в формате .csv.
  - Предобработка данных, включающая в себя удаление строк с нулевыми значениями, обработку категориальных данных при наличии, нормализацию и дробление на тестовую и обучающую выборки. Полученные выборки передаются в следующие компоненты обучения и тестирования модели.
  - Обучение модели логистической регрессии и сохранение модели в пикл-файле.
  - Тестирование модели для получения метрик с сохранением метрик в формате .json.
    
### Схема пайплайна.


## 2. Разработка ETL-компонентов.

### Load.py

### Preprocessing.py

### Training.py

### Evaluation.py


## 3. Оркестрация пайплайна с помощью Airflow.
### /dags/main.py

### Описание зависимостей

### Описание логирования


## 4. Выгрузка результатов на локальный диск.
### /results/

## 5. Анализ ошибок и устойчивости.
### Где может "упасть" процесс?

### Описание исключений

