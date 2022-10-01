from analysis import Node, Collection
from .Connection import Connection
class Objective(Node):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._connections = list[Connection]()

    def connect(self, collection:Collection, weight=1.0):
        c = Connection(self, collection, weight)
        if c not in self._connections:
            self._connections.append(c)
    @property
    def connections(self):
        return self._connections