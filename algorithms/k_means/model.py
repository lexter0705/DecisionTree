from numpy import ndarray
from algorithms.abstract_model.model import Model


class KMeans(Model):
    def predict(self, x: ndarray) -> ndarray:
        pass