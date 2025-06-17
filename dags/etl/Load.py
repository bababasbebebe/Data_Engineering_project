import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

def load_data():
    try:
        logger.info(f"Начало загрузки данных load_breast_cancer")

        features = pd.DataFrame(load_breast_cancer().data, columns=load_breast_cancer().feature_names)

        # Сохранение info
        pd.DataFrame({"Column": features.columns, "Non-Null Count": len(features) - features.isnull().sum().values,
                      "Dtype": features.dtypes.values}).to_csv("features_info.csv")

        # Сохранение describe
        features.describe().to_csv('features_describe.csv')

        target = pd.DataFrame(load_breast_cancer()['target'], columns=['target'])
        target.hist()

        # Сохранение распределения target
        plt.savefig('figure.pdf')

        logger.info(f"Данных успешно загружены и info, describe и распределение target сохранено")

        return features, target

    except Exception as e:
        logger.error(f"Ошибка при загрузке данных: {str(e)}")
        raise