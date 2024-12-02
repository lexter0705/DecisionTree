from algorithms.decision_tree.additional_modules.condition import Condition
from algorithms.decision_tree.additional_modules.node_statistic import NodeStatistic


class Node:
    def __init__(self, condition: Condition, statistic: NodeStatistic):
        self.__condition = condition
        self.__statistic = statistic

    @property
    def statistic(self) -> NodeStatistic:
        return self.__statistic

    @property
    def condition(self):
        return self.__condition

