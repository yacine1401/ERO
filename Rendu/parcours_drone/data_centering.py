import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt
import sys

city = ox.graph_from_place(sys.argv[1] + ", Montreal, CANADA", network_type="drive")
#ox.plot_graph(city, node_color="r")

#print("---Eulerization de city---")
G = nx.Graph(city)
g = nx.eulerize(G)

#print("---Fin Eulerization de city---")
#print(time.localtime(time.time()))

#print("---Debut de Eulerian circuit---")

res = list(nx.eulerian_circuit(g))
edges = list(city.edges(keys=True, data=True))

length = 0

for e in res:
    for edge in edges:
        if (e == (edge[0], edge[1])):
            length += edge[3]['length']
            print(edge[3])


#print("---Fin de Eulerian circuit---")
#print(time.localtime(time.time()))

moyenne = []
x = res[0][0]
y = res[0][1]

for i in range(len(res)):
    if (res[i][0] < x):
        x = res[i][0]
    if (res[i][1] < y):
        y = res[i][1]

moyenne.append(x / len(res))
moyenne.append(y / len(res))

V_x = 0
V_y = 0
for i in range(len(res)):
    V_x += (res[i][0] - x / len(res)) ** 2 / len(res)
    V_y += (res[i][1] - y / len(res)) ** 2 / len(res)

e_x = math.sqrt(V_x)
e_y = math.sqrt(V_y)

for i in range(len(res)):
    res[i] = [round((res[i][0] - moyenne[0]) * 100 / e_x), round((res[i][1] - moyenne[1]) * 100 / e_y)]
    print(i, ": ", res[i])


print(round(length) / 1000, "Km a parcourir dans le quartier", sys.argv[1], ".")
print("Pour un cout de", round(length / 1000) / 100, "euros et 100 euros de locations.")
