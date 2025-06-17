from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import logging

logger = logging.getLogger(__name__)

def preprocess(features, target):
    try:
        logger.info(f"Начало обработки данных")

        features = features.dropna()

        # Обработка категориальных данных
        is_cat = features.dtypes.values == 'object'
        cat_cols = []
        for i in range(features.shape[1]):
            if is_cat[i]:
                cat_cols.append(features.columns[i])
        if len(cat_cols) != 0:
            le = LabelEncoder()
            features[cat_cols] = le.fit_transform(features[cat_cols])

        X = features.values
        y = target

        # Нормализация
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        logger.info(f"Данные успешно обработаны")

        return train_test_split(X, y, test_size=0.2)

    except Exception as e:
        logger.error(f"Ошибка при обработке данных: {str(e)}")
        raise
