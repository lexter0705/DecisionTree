from numpy import ndarray
from base.model import Model
from node import DecisionTreeNode
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