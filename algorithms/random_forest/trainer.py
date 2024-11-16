from numpy import ndarray
from algorithms.random_forest.model import RandomForest
from base.metrics import Metrics
from base.trainer import ModelTrainer


class RandomForestCreator(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (RandomForest, Metrics):
        pass
