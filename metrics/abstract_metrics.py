import abc


class Metrics(abc.ABC):
    @abc.abstractmethod
    def plot_metrics(self):
        pass

    @abc.abstractmethod
    def get_metrics(self) -> dict[str, float]:
        pass