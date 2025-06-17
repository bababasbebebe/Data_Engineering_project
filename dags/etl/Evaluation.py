from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import joblib
import json
import logging

logger = logging.getLogger(__name__)

def evaluate(X_test, y_test, model_name: str, metrics_name: str):
    try:
        logger.info(f"Начало тестирования модели")

        # Загрузка модели
        model = joblib.load(model_name + '.pkl')
        logger.info(f"Модель {model_name} успешно загружена")

        y_pred = model.predict(X_test)

        # Сохранение метрик в .json
        metrics = {"accuracy": accuracy_score(y_test, y_pred), "precision": precision_score(y_test, y_pred),
                      "recall": recall_score(y_test, y_pred), "f1": f1_score(y_test, y_pred)}

        with open(metrics_name + '.json', 'w') as f:
            json.dump(metrics, f)

        logger.info(f"Метрики \n {metrics} \n успешно сохранены в {metrics_name + '.json'}")

    except Exception as e:
        logger.error(f"Ошибка при загрузке данных: {str(e)}")
        raise