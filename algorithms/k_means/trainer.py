from numpy import ndarray
from algorithms.k_means.model import KMeans
from metrics.abstract_metrics import Metrics
from algorithms.abstract_model.trainer import ModelTrainer


class KMeansTrainer(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (KMeans, Metrics):
        pass
