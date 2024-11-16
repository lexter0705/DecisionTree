from numpy import ndarray
from algorithms.abstract_model.model import Model


class RandomForest(Model):
    def predict(self, x: ndarray) -> ndarray:
        pass