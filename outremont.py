import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt

city = ox.graph_from_place("Outremont, Montreal, CANADA", network_type="drive")
#ox.plot_graph(city, node_color="r")

print("---Eulerization de city---")
G = nx.Graph(city)
#nx.draw(G, with_labels=True)
plt.show()
print(G)
g = nx.eulerize(G)

print("---Fin Eulerization de city---")
print(time.localtime(time.time()))

print("---Debut de Eulerian circuit---")

res = nx.eulerian_circuit(g)

# Affiche le circuit eulerien

circuit = nx.to_networkx_graph(res)
#nx.draw(circuit)
#plt.show()

res = list(res)
print("---Fin de Eulerian circuit---")
print(time.localtime(time.time()))


print("---Debut calcul chemin deneigeuse---")

def return_missing_target(edges, missing_edges, source):
    for i in missing_edges:
        if (i[0] == source):
            return i[1]
    return None

def chemin_deneigeuse():
    nodes = list(G.nodes)
    edges = list(G.edges)
    sommet_parcouru = []
    edge_parcouru = []
    source = nodes[0]
    missing_edges = edges

    sommet_parcouru.append(source)
    nb_edges = len(edges)
    nb_uniqueparcours = 0
    prev_uniqueparcours = -1
    while nb_uniqueparcours < nb_edges:
        if prev_uniqueparcours == nb_uniqueparcours:
            target_missing = return_missing_target(edges, missing_edges, source)
            if target_missing != None:
                nb_uniqueparcours += 1
                edge_parcouru.append((source, target_missing))
                source = target_missing
                prev_uniqueparcours = nb_uniqueparcours
                continue

        prev_uniqueparcours = nb_uniqueparcours
        print("Avancement:", nb_uniqueparcours * 100 / nb_edges)

        # Calcule le chemin le plus court avec tous les autres noeuds
        shortest_path = nx.single_source_shortest_path(G, source)
        for target, path in shortest_path.items():
            # Ajoute tous les edges
            if target in sommet_parcouru:
                if len(sommet_parcouru) == len(nodes):
                    sommet_parcouru = []
                else:
                    continue

            for i in range(len(path) - 1):
                edge = (path[i], path[i+1])
                inv_edge = (path[i+1], path[i])

                if edge not in edge_parcouru and inv_edge not in edge_parcouru:
                    nb_uniqueparcours += 1
                edge_parcouru.append(edge)

                if edge in missing_edges:
                    missing_edges.remove(edge)

            source = target
            if not source in sommet_parcouru:
                sommet_parcouru.append(source)
            break
    return edge_parcouru

# Print le chemin du graph
chemin = chemin_deneigeuse()
nx.draw(G,pos=nx.spring_layout(G), edgelist=chemin)
plt.show()

# Check le nombre de rues manquantes
edges = list(G.edges)
nb_missing_edges = 0
for edge in edges:
    inv_edge = edge[::-1]
    if edge not in chemin and inv_edge not in chemin:
        nb_missing_edges += 1

print("Pourcentage de rues manquantes:", nb_missing_edges * 100 / len(edges))