
from .Edge import Edge 
from .Node import Node 
import os 
class Graph:

    def __init__(self) -> None:
        self._edges = list[Edge]()
        self._nodes = list[Node]()
        pass

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, objs):
        for n in objs:
            if n not in self._nodes:
                self._nodes.append(n)
            for e in n.connections:
                if e not in self._edges:
                    self._edges.append(e)

    @property
    def gv(self, template=None):
        from jinja2 import Template
        shapes = dict(
            Collection='folder',
            Metric='note',
            default='box'
        )
        if template is None:
            template = os.path.join(os.path.dirname(__file__),'analysis.gv.j2')
        with open(template) as template:
            return Template(template.read()).render(
                nodes=self.nodes,
                edges=self.edges,
                shapes=shapes
            )