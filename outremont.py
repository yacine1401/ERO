import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt

city = ox.graph_from_place("Outremont, Montreal, CANADA", network_type="drive")
#ox.plot_graph(city, node_color="r")

print("---Eulerization de city---")
G = nx.Graph(city)
nx.draw(G, with_labels=True)
plt.show()
print(G)
g = nx.eulerize(G)

print("---Fin Eulerization de city---")
print(time.localtime(time.time()))

print("---Debut de Eulerian circuit---")

res = list(nx.eulerian_circuit(g))
print("---Fin de Eulerian circuit---")
print(time.localtime(time.time()))

print(res)

route = []
for link in res:
    route.append(link[0])


fig, ax = ox.plot_graph_route(city, res)