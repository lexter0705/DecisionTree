from numpy import ndarray
from algorithms.decision_tree.model import DecisionTree
from base.metrics import Metrics
from base.trainer import ModelTrainer


class DecisionTreeCreator(ModelTrainer):
    def __init__(self):
        pass

    def __create_decision_tree(self):
        pass

    def train_model(self, x: ndarray, y: ndarray) -> (DecisionTree, Metrics):
        pass
