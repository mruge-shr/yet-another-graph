from uuid import uuid4 
from .Node import Node 

class Edge:

    def __init__(self, n1:Node, n2:Node, id=None) -> None:
        self.id = id or str(uuid4().hex)
        self.n1 = n1 
        self.n2 = n2

    def __eq__(self, other) -> bool:
        if self.id == other.id:
            return True
        return False

    @property 
    def members(self):
        return self.n1, self.n2