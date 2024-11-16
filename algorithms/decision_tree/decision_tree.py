from node import DecisionTreeNode
import numpy as np
import pandas as pd


class DecisionTree:
    def __init__(self, tree: list[DecisionTreeNode, int]):
        self.__tree = tree

    def __classify_one_element(self, element: np.ndarray) -> int:
        answers = []
        for i in self.__tree:
            pass

    def classify(self, dataset_for_classify: pd.DataFrame | np.ndarray) -> np.ndarray:
        pass