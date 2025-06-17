from sklearn.linear_model import LogisticRegression
import joblib
import logging

logger = logging.getLogger(__name__)

def train_model(X_train, y_train, model_name: str):
    try:
        logger.info(f"Начало обучения модели")

        # Модель LogisticRegression
        model = LogisticRegression()
        model.fit(X_train, y_train.ravel())

        # Сохранение модели
        joblib.dump(model, model_name + '.pkl')
        logger.info(f"Модель {model_name} сохранена. ")

        return model_name + '.pkl'
        
    except Exception as e:
        logger.error(f"Ошибка при обучении модели: {str(e)}")
        raise
