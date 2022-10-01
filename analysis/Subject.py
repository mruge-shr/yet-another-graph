from .Node import Node
from .Option import Option
from .Edge import Edge

class Subject(Node):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.options = list[Option]()

    def add_option(self, option):
        if option not in self.options:
            self.options.append(option)

    @property
    def connections(self):
        return [Edge(option,self) for option in self.options]