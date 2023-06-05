import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt

start = time.time()

arrondissements = [
    "Ahuntsic-Cartierville",
    "Anjou",
    "Côte-des-Neiges–Notre-Dame-de-Grâce",
    "Lachine",
    "LaSalle",
    "Le Plateau-Mont-Royal",
    "Le Sud-Ouest",
    "L'Île-Bizard–Sainte-Geneviève",
    "Mercier-Hochelaga-Maisonneuve",
    "Montréal-Nord",
    "Outremont",
    "Pierrefonds-Roxboro",
    "Rivière-des-Prairies–Pointe-aux-Trembles",
    "Rosemont–La Petite-Patrie",
    "Saint-Laurent",
    "Saint-Léonard",
    "Verdun",
    "Ville-Marie",
    "Villeray–Saint-Michel–Parc-Extension",
]

length = 0

def chemin_drone():
    circuits = []
    for arrondissement in arrondissements:
        print("Arrondissement :", arrondissement)
        data = ", Montreal, CANADA"
        data = arrondissement + data
        g = ox.graph_from_place(data, network_type="drive")
        G = nx.Graph(g)
        g_eulerize = nx.eulerize(G)
        res = list(nx.eulerian_circuit(g_eulerize))
        circuits.append(res)

        for e in res:
            for edge in edges:
                if (e == (edge[0], edge[1])):
                    length += edge[3]['length']

    return circuits

circuits = chemin_drone()
end = time.time()
elapsed = (end - start) / 100
print(f'Temps d\éxécution : {elapsed:.2}s')
print(round(length) / 1000, "Km a parcourir dans Montréal", sys.argv[1], ".")
print("Pour un cout de", round(length / 1000) / 100, "euros et 100 euros de locations.")
