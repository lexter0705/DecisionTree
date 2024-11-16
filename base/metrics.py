import abc


class Metrics(abc.ABC):
    @abc.abstractmethod
    def plot_metrics(self):
        pass