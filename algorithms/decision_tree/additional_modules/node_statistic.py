from attr import dataclass


@dataclass
class NodeStatistic:
    error: float
    percent_left: float
    percent_right: float
