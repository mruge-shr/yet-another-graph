from .Node import Node 
from .Score import Score
from .Edge import Edge

class Metric(Node):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.scores = list[Score]()

    def add_score(self, name, value):
        s = Score(name, self, value)
        if s not in self.scores:
            self.scores.append(s)
        return s

    def get_score(self, name):
        for score in self.scores:
            if score.name == name:
                return score
        return min(self.scores)

    @property
    def connections(self):
        return [Edge(self,score) for score in self.scores]

    