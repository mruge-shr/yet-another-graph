from .Metric import Metric
from .Connection import Connection
from .Node import Node

class Collection(Node):

    def __init__(self, **kwargs) -> None:
        self._connections = list[Connection]()
        super().__init__(**kwargs)

    def connect(self, metric: Metric, weight: float):
        c = Connection(self, metric, weight)
        self._connections.append(c)

    @property
    def connections(self):
        return self._connections
