import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

logger = logging.getLogger(__name__)

def load_data():
    try:
        logger.info(f"Начало загрузки данных load_breast_cancer")

        features = pd.DataFrame(load_breast_cancer().data, columns=load_breast_cancer().feature_names)
        if features.empty:
            raise ValueError("Данные пусты!")
            
        # Сохранение info
        pd.DataFrame({"Column": features.columns, "Non-Null Count": len(features) - features.isnull().sum().values,
                      "Dtype": features.dtypes.values}).to_csv(os.path.join(RESULTS_DIR, 'features_info.csv'), index=False)
        
        # Сохранение describe
        features.describe().to_csv(os.path.join(RESULTS_DIR, 'features_describe.csv'), index=False)

        target = pd.DataFrame(load_breast_cancer()['target'], columns=['target'])
        if target.empty:
            raise ValueError("Данные пусты!")
            
        target.hist()

        # Сохранение распределения target
        plt.savefig(os.path.join(RESULTS_DIR, 'features.csv'), index=False)

        logger.info(f"Данных успешно загружены и info, describe и распределение target сохранено")

        return features, target

    except Exception as e:
        logger.error(f"Ошибка при загрузке данных: {str(e)}")
        raise
