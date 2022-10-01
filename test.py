from analysis import *
from analysis.Objective import Objective
g = Graph()


met_cost = Metric(friendly='Base Cost')
met_cost.add_score('0-1000',1)
met_cost.add_score('1000-2000',5)
met_cost.add_score('2000-3000',10)

met_life = Metric(friendly='lifespan')
met_life.add_score('1yr',1)
met_life.add_score('2yr',5)
met_life.add_score('3yr',10)

met_ram = Metric(friendly='Ram')
met_ram.add_score('4GB',1)
met_ram.add_score('8GB',2)
met_ram.add_score('16GB',4)

met_cpu = Metric(friendly='CPU')
met_cpu.add_score('2c',1)
met_cpu.add_score('4c',2)
met_cpu.add_score('16c',4)

met_weight = Metric(friendly='Weight')
met_weight.add_score('<5lbs',1)
met_weight.add_score('>5lbs',2)

met_screen = Metric(friendly='Screen Size')
met_screen.add_score('14in',2)
met_screen.add_score('16in',2)

coll_cost = Collection(friendly="Cost")
coll_cost.connect(met_cost, 100)
coll_cost.connect(met_ram, 10)
coll_cost.connect(met_cpu, 10)
coll_cost.connect(met_screen, 10)
coll_cost.connect(met_life,20.0)

coll_perf = Collection(friendly="Performance")
coll_perf.connect(met_cpu, 10)
coll_perf.connect(met_ram, 20)

coll_aesthetic = Collection(friendly="Aesthetic")
coll_aesthetic.connect(met_weight, 10)
coll_aesthetic.connect(met_screen, 10)

mission = Objective(friendly="Mission")
mission.connect(coll_cost, 10.0)
mission.connect(coll_perf, 15.0)
mission.connect(coll_aesthetic, 5.0)


mac = Subject(friendly='MAC')
mac.add_option(
    Option(friendly='8GB').score(met_ram.get_score('8GB')))
mac.add_option(
    Option(friendly='16GB').score(met_ram.get_score('16GB')))
mac.add_option(
    Option(friendly='16c').score(met_cpu.get_score('16c')))
mac.add_option(
    Option(friendly='renewal').score(met_life.get_score('2yr')))


dell = Subject(friendly='DELL')
dell.add_option(
    Option(friendly='8GB').score(met_ram.get_score('8GB')))
dell.add_option(
    Option(friendly='16GB').score(met_ram.get_score('16GB')))
dell.add_option(
    Option(friendly='32GB').score(met_ram.get_score('16GB')))
dell.add_option(
    Option(friendly='16c').score(met_cpu.get_score('16c')))
dell.add_option(
    Option(friendly='64c').score(met_cpu.get_score('16c')))
dell.add_option(
    Option(friendly='renewal').score(met_life.get_score('3yr')))


import gc
g.nodes = [obj for obj in gc.get_objects() if isinstance(obj, Node)]


with open('mygraph.gv', 'w') as f:
    f.write(g.gv)