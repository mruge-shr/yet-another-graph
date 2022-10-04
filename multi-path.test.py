import uuid, jinja2
class Edge:
    def __init__(self, a, b, cost=0, operation='none'):
        self.a = a
        self.b = b 
        self.cost = cost
        self.op = operation.upper()

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

def filter(paths):
    groups = []
    constraints = [e for e in edges if e.op != 'none']
    for c in constraints:
        if c.op == 'OR':
            groups += [p for p in paths if p.contains(c.a) and p.not_contains(c.b)]
            groups += [p for p in paths if p.not_contains(c.a) and p.contains(c.b)]



# car = Node('car')
# lx = Node('lx')
# ls = Node('ls')
# features = Node('Features')
# cost = Node('cost')
# goal = Node('goal')
# base = Node('basecost')

# e1 = Edge(car, lx)
# e2 = Edge(car, ls)
# c1 = Edge(lx, ls, operation='or')

# e3 = Edge(ls, cost, -1)
# e4 = Edge(lx, cost, -2)
# e5 = Edge(ls, features, 5)
# e6 = Edge(lx, features, 9)

# e7 = Edge(cost, goal, 0)
# e8 = Edge(features, goal, 0)

# e10 = Edge(car, base)
# e11 = Edge(base, cost, -10)
# import gc
# nodes = [obj for obj in gc.get_objects() if isinstance(obj, Node)]
# edges = [obj for obj in gc.get_objects() if isinstance(obj, Edge)]


# paths = all_paths(goal, car)
# groups = filter(paths)



mac = Node('Mac')
s1 = Node('8gb')
s2 = Node('16gb')
s3 = Node('4c')
s4 = Node('8c')
s5 = Node('$2k')


mem = Node('mem')
cpu = Node('cpu')
cost = Node('cost')


group_cost = Node('cost')
perf = Node('performance')

edges = []
edges += [Edge(mac, s1)]
edges += [Edge(mac, s2)]
edges += [Edge(mac, s3)]
edges += [Edge(mac, s4)]
edges += [Edge(mac, s5)]
edges += [Edge(s1, mem, 8)]
edges += [Edge(s2, mem, 16)]
edges += [Edge(s3, cpu, 4)]
edges += [Edge(s4, cpu, 8)]

edges += [Edge(s1, cost, 1)]
edges += [Edge(s2, cost, 8)]
edges += [Edge(s3, cost, 1)]
edges += [Edge(s4, cost, 2)]
edges += [Edge(s5, cost, 200)]

edges += [Edge(mem, perf, 1)]
edges += [Edge(cpu, perf, 1)]
edges += [Edge(cost, group_cost, 1)]
goal = Node('goal')
edges += [Edge(group_cost, goal)]
edges += [Edge(perf, goal)]


import gc
nodes = [obj for obj in gc.get_objects() if isinstance(obj, Node)]
# edges = [obj for obj in gc.get_objects() if isinstance(obj, Edge)]
j2 = """
digraph {
    {% for node in nodes %}
    id_{{node.id}} [label="{{node.name}}"]
    {%- endfor %}

    {% for edge in edges %}
    {% if edge.op == 'or' %}
    id_{{edge.a.id}} -> id_{{edge.b.id}} [style="dashed" label="OR"]
    {% else %}
    id_{{edge.a.id}} -> id_{{edge.b.id}} [label="{{edge.cost}}"]
    {% endif %}
    {%- endfor %}
}"""
with open('testgraph.gv', 'w') as f:
    f.write(jinja2.Template(j2).render(nodes=nodes, edges=edges))

