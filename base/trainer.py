import abc
from numpy import ndarray
from base.metrics import Metrics
from base.model import Model


class ModelTrainer(abc.ABC):
    @abc.abstractmethod
    def train_model(self, x: ndarray, y: ndarray) -> (Model, Metrics):
        pass