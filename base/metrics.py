import abc
from base.model import Model


class Metrics(abc.ABC):
    def __init__(self, model: Model):
        self.model = model
        self.__calculate_metrics__()

    @abc.abstractmethod
    def __calculate_metrics__(self):
        pass

    @abc.abstractmethod
    def plot_metrics(self):
        pass