from numpy import ndarray
from algorithms.abstract_model.model import Model
from algorithms.decision_tree.additional_modules.node import DecisionTreeNode
import numpy as np


class DecisionTree(Model):
    def __init__(self, tree: list[DecisionTreeNode, int]):
        self.__tree = tree

    def __classify_one_element(self, element: np.ndarray) -> int:
        answers = []
        for i in self.__tree:
            pass

    def predict(self, x: ndarray) -> ndarray:
        pass