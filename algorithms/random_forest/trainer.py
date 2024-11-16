from numpy import ndarray
from algorithms.random_forest.model import RandomForest
from metrics.abstract_metrics import Metrics
from algorithms.abstract_model.trainer import ModelTrainer


class RandomForestTrainer(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (RandomForest, Metrics):
        pass
