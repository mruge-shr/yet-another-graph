
from uuid import uuid4


class Node:

    def __init__(self, friendly=None, id=None) -> None:
        self.id = id or str(uuid4().hex)
        self.friendly = friendly or self.id[:4]

    def __eq__(self, other) -> bool:
        if self.id == other.id:
            return True
        return False

    @property
    def connections(self):
        return []