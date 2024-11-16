import abc
from numpy import ndarray


class Model(abc.ABC):
    @abc.abstractmethod
    def predict(self, x: ndarray) -> ndarray:
        pass
