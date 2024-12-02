from numpy import ndarray

from algorithms.decision_tree.additional_modules.node import Node


class Condition:
    def __init__(self, value: float, right: Node | int, left: Node | int, id_checked_value: int):
        self.__value = value
        self.__right = right
        self.__left = left
        self.__id_checked_value = id_checked_value

    def get_next(self, row: ndarray[float | int]) -> Node | int:
        if self.__value > row[self.__id_checked_value]:
            return self.__left

        return self.__right
