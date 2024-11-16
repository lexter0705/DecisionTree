from numpy import ndarray
from algorithms.k_means.model import KMeans
from base.metrics import Metrics
from base.trainer import ModelTrainer


class KMeansCreator(ModelTrainer):
    def __init__(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (KMeans, Metrics):
        pass
