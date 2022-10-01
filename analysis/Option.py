from .Node import Node 
from .Edge import Edge
from .Score import Score

class Option(Node):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.requirements = list[Option]()
        self._score:Score = None

    def score(self, score):
        self._score = score
        return self

    @property
    def connections(self):
        return [Edge(self,r) for r in self.requirements] + \
                [Edge(self._score,self)]