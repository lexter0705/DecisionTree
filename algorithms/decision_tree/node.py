import numpy as np
import pandas as pd


class DecisionTreeNode:
    def __init__(self, condition_value: float, column_id: int, error: float = None, count_elements: list[int] = None):
        self.__condition_value = condition_value
        self.__column_id = column_id
        self.__error = error
        self.__count_elements = count_elements

    def is_less(self, series: list | pd.Series | np.ndarray) -> bool:
        if series is np.ndarray and series.ndim != 1:
            raise ValueError("series will be one-dimensional")

        if not (series is np.ndarray or series is pd.Series or series is list):
            raise ValueError(f"data type {type(series)} not supported ")

        if len(series) - 1 <= self.__column_id:
            raise ValueError(f"index {self.__column_id} out of range")

        return series[self.__column_id] < self.__condition_value

    def get_stats(self):
        return [self.__error, self.__count_elements, self.__condition_value]