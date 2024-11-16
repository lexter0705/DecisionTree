import numpy as np


class DecisionTreeNode:
    def __init__(self, condition_value: float, column_id: int, error: float = None, count_elements: list[int] = None):
        self.__condition_value = condition_value
        self.__column_id = column_id
        self.__error = error
        self.__count_elements = count_elements

    def is_less(self, series: np.ndarray[int]) -> bool:
        if series is not np.ndarray:
            raise ValueError(f"data type {type(series)} not supported ")

        return series[self.__column_id] < self.__condition_value

    def get_stats(self):
        return [self.__error, self.__count_elements, self.__condition_value]