import osmnx as ox
from city import city
import networkx as nx
import math
import time
print(city)
print(type(city))
edges = list(city.edges)
print(len(edges))
#print(list(city.edges))
#ox.plot_graph(city, node_color="r")
path = nx.shortest_path(city, list(city.nodes)[0])

src = list(city.nodes)[0]
print(type(path))
print(len(path))
#print(path[0])

print(time.localtime(time.time()))

##Calcul de la length min: 
'''print("------- calcul de la matrices des distances--------")
mat_distances = dict(nx.all_pairs_shortest_path_length(city))
print("------- fin Du calcul de la matrices des distances--------")
d_min = math.inf
way_min = []
print("------- Debut de la boucle for---------")
for target,way in path.items():
    d = mat_distances[src][target]
    if d == 0:
        print(src)
        print(target)
    elif d < d_min:
        d_min = d
        way_min = way

print(d_min)
print(way_min)
print(time-localtime(time-time()))'''

print("---Eulerization de city---")
G = nx.Graph(city)
print(G)
g = nx.eulerize(G)
with open('eulerized.txt', 'w') as f:
    f.write('\n'.join(g))

print("---Fin Eulerization de city---")
print(time.localtime(time.time()))

print("---Debut de Eulerian circuit---")

res = nx.eulerian_circuit(g)
print("---Fin de Eulerian circuit---")
print(time.localtime(time.time()))

print(res)
