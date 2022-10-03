import uuid, jinja2
class Edge:
    def __init__(self, a, b, cost=0):
        self.a = a
        self.b = b 
        self.cost = cost 
    def __str__(self):
        return f"{self.a.name} -> {self.b.name} : {self.cost}"

class Node:
    def __init__(self, name=""):
        self.name = name
        self.id = str(uuid.uuid4().hex)
    def __eq__(self, other):
        return self.id == other.id
    def __str__(self):
        return f"{self.name}"

class Path:
    def __init__(self,edges=[]):
        if isinstance(edges, Edge):
            self.edges = [edges]
        else:
            self.edges = edges

    def __add__(self, edge):
        return Path(self.edges + [edge])

    def __str__(self):
        return '->'.join([str(e.b) for e in self.edges])+f": {self.cost}"

    @property
    def head(self):
        return self.edges[0].a

    @property
    def tail(self):
        return self.edges[-1].b

    @property
    def cost(self):
        return sum([e.cost for e in self.edges])

    def index(self, i):
        return self.edges[i].a

    def endswith(self, node):
        return self.tail == node

    def not_contains(self, node):
        return node not in self.nodes

def get_node(id):
    for node in nodes:
        if node.id == id:
            return node

def all_paths(goal, paths):
    if isinstance(paths, list):
        path = paths.pop(0)
        new_paths = [path+e for e in edges if e.a == path.tail]
        if len(new_paths) == 0:
            return paths + [path]
        return all_paths(goal,paths + new_paths)
    else:
        return all_paths(goal,[Path(e) for e in edges if e.a == paths])


def aggregate(paths):
    options = {}
    for path in paths:
        options[path.index(1).id] = options.get(path.index(1).id, 0) + path.cost
    return options

    

car = Node('car')
lx = Node('lx')
ls = Node('ls')
features = Node('Features')
cost = Node('cost')
goal = Node('goal')

e1 = Edge(car, lx)
e2 = Edge(car, ls)

e3 = Edge(ls, cost, 2)
e4 = Edge(lx, cost, 3)
e5 = Edge(ls, features, 2)
e6 = Edge(lx, features, 3)

e7 = Edge(cost, goal, -100)
e8 = Edge(features, goal, 100)

import gc
nodes = [obj for obj in gc.get_objects() if isinstance(obj, Node)]
edges = [obj for obj in gc.get_objects() if isinstance(obj, Edge)]


paths = all_paths(goal, car)
options = aggregate(paths)
# print(f"mypaths: {[str(p) for p in paths]}")
for option in options:
    print(f"{get_node(option)}: {options[option]}")

# for path in :
#     print(path)




j2 = """
digraph {

    {% for node in nodes %}
    id_{{node.id}} [label="{{node.name}}"]
    {%- endfor %}

    {% for edge in edges %}
    id_{{edge.a.id}} -> id_{{edge.b.id}} [label="{{edge.cost}}"]
    {%- endfor %}
}"""
with open('testgraph.gv', 'w') as f:
    f.write(jinja2.Template(j2).render(nodes=nodes, edges=edges))

