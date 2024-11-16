from numpy import ndarray
from algorithms.decision_tree.model import DecisionTree
from metrics.abstract_metrics import Metrics
from algorithms.abstract_model.trainer import ModelTrainer


class DecisionTreeTrainer(ModelTrainer):
    def __init__(self):
        pass

    def __create_decision_tree(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (DecisionTree, Metrics):
        pass
