from numpy import ndarray
from base.model import Model


class Regression(Model):
    def predict(self, x: ndarray) -> ndarray:
        pass