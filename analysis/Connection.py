from .Edge import Edge
from .Node import Node 

class Connection(Edge):
    
    def __init__(self, src:Node, dst:Node, weight=10.0, **kwargs) -> None:
        super().__init__(n1=src, n2=dst, **kwargs)
        self.weight = weight


