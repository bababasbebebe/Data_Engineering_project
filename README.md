# Data_Engineering_project
Экзаменационная работа 

## 0. Логика репозитория
- [**dags/**](./dags/):
  - Файл [main.py](./dags/main.py) с оркестрацией пайплайна.
  - [etl/](./dags/etl) с файлами ETL-компонентов:
    - Файл [Load.py](./dags/etl/Load.py) с функцией загрузки и сохранения информации о данных.
    - Файл [Preprocessing.py](./dags/etl/Preprocessing.py) с функцией предобработки данных и разбития на выборки.
    - Файл [Training.py](./dags/etl/Training.py) с функцией обучения и сохранения модели.
    - Файл [Evaluation.py](./dags/etl/Evaluation.py) с функцией тестирования модели, вычисления и сохранения метрик.
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
      
## 1. Планирование пайплайна.
### Описание датасета.

### Описание структуры пайплайна.

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

