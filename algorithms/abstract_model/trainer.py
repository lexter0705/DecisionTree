import abc
from typing import Tuple
from numpy import ndarray
from metrics.abstract_metrics import Metrics
from algorithms.abstract_model.model import Model


class ModelTrainer(abc.ABC):
    @abc.abstractmethod
    def train_model(self, x: ndarray, y: ndarray) -> Tuple[Model, Metrics]:
        pass