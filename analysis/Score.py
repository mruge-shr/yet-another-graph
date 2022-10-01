from .Node import Node 
from .Edge import Edge
from analysis import Metric, Score

class Score(Node):

    def __init__(self, name:str, metric:Metric, value, **kwargs) -> None:
        super().__init__(friendly=name, **kwargs)

        self.metric = metric
        self.name = name
        self.value = value


    def __lt__(self, other:Score):
        return self.value < other.value

    # @property
    # def connections(self):
    #     return [Edge(self, self.metric)]