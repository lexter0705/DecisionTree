from numpy import ndarray
from algorithms.regression.model import Regression
from metrics.abstract_metrics import Metrics
from algorithms.abstract_model.trainer import ModelTrainer


class RegressionTrainer(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (Regression, Metrics):
        pass
