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
    def __init__(self, name="", id=None):
        self.name = name
        if not id:
            self.id = str(uuid.uuid4().hex)
        else:
            self.id = id
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

    def __iter__(self):
        node_list = []
        [node_list.append(n) for e in self.edges for n in [e.a, e.b] if n not in node_list ]
        for n in node_list: yield n

    @property
    def head(self):
        return self.edges[0].a

    @property
    def option(self):
        return self.edges[0].b

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

    # def contains(self, node):
    #     return node in self.nodes

    # def not_contains(self, node):
    #     return node not in self.nodes

class Flow:
    def __init__(self, paths):
        self.paths = paths

    def split(self, n1, n2):
        return (
            Flow([p for p in self.paths if n1 not in p]),
            Flow([p for p in self.paths if n2 not in p])
        )

    def __str__(self):
        return ','.join(self.options)
        return str(len(f"paths: {len(self.paths)}"))
        return '\n'.join([str(p) for p in self.paths])
    
    @property
    def cost(self):
        return sum([p.cost for p in self.paths])

    @property
    def options(self):
        uniq = []
        return set([p.option.name for p in self.paths])

    @property
    def count(self):
        return len(self.paths)

def get_node(id):
    for node in nodes:
        if node.id == id:
            return node

# def filter(paths, constraint, invert=False):


# def all_flows(all_paths, constraints):
#     flows = []
    
#     for c1 in constraints:
#         paths_with = filter(paths, c1)
#         paths_without = filter(paths, c1, invert=True)
#         for c2 in [c for c in constraints if c not c1]:
#             flows += Flow(filtered)

def all_paths(goal, paths):
    if isinstance(paths, list):
        path = paths.pop(0)
        new_paths = [path+e for e in edges if e.a == path.tail]
        if len(new_paths) == 0:
            return paths + [path]
        return all_paths(goal,paths + new_paths)
    else:
        return all_paths(goal,[Path(e) for e in edges if e.a == paths])

def paths_contain(paths, node):
    return [p for p in paths if p.contains(node)]


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
goal = Node('goal')
edges = [
    Edge(mac, s1),
    Edge(mac, s2),
    Edge(mac, s3),
    Edge(mac, s4),
    Edge(mac, s5),
    Edge(s1, mem, 8),
    Edge(s2, mem, 16),
    Edge(s3, cpu, 4),
    Edge(s4, cpu, 8),

    Edge(s1, cost, 1),
    Edge(s2, cost, 8),
    Edge(s3, cost, 1),
    Edge(s4, cost, 2),
    Edge(s5, cost, 200),

    Edge(mem, perf, 1),
    Edge(cpu, perf, 1),
    Edge(cost, group_cost, 1),

    Edge(group_cost, goal),
    Edge(perf, goal),
]
import gc
nodes = [obj for obj in gc.get_objects() if isinstance(obj, Node)]
constraints = [
    (s1, s2),
    (s3, s4)
]

paths = all_paths(nodes[9],nodes[0])
flows = [Flow(paths)]

for c in constraints:
    new_flows = []
    for i in range(len(flows)):
        f = flows.pop()
        f1, f2 = f.split(*c)
        # print(f"{f} => {f1},{f2}")
        new_flows.append(f1)
        new_flows.append(f2)
    flows = new_flows


for flow in flows:
    print(flow, flow.cost)
    print("---")


### CONSTRAINT TEST ###
# nodes = [Node(i) for i in range(10)]
# edges = [
#     Edge(nodes[0],nodes[1],1),
#     Edge(nodes[0],nodes[2],1),
#     Edge(nodes[0],nodes[3],1),
#     Edge(nodes[0],nodes[4],1),
#     Edge(nodes[1],nodes[5],1),
#     Edge(nodes[2],nodes[6],1),
#     Edge(nodes[3],nodes[7],1),
#     Edge(nodes[4],nodes[8],1),
#     Edge(nodes[5],nodes[9],1),
#     Edge(nodes[6],nodes[9],1),
#     Edge(nodes[7],nodes[9],1),
#     Edge(nodes[8],nodes[9],1),
# ]
# constraints = [
#     (nodes[1], nodes[2]),
#     (nodes[3], nodes[4])
# ]

# paths = all_paths(nodes[9],nodes[0])
# flows = [Flow(paths)]

# for c in constraints:
#     for i in range(len(flows)):
#         f = flows.pop()
#         f1, f2 = f.split(*c)
#         flows.append(f1)
#         flows.append(f2)




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


