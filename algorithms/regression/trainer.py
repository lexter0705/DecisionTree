from numpy import ndarray
from algorithms.regression.model import Regression
from base.metrics import Metrics
from base.trainer import ModelTrainer


class RegressionTrainer(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (Regression, Metrics):
        pass
