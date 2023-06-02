import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt

print(time.localtime(time.time()))

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


def chemin_drone():
    circuits = []
    for arrondissement in arrondissements:
        print("Arrondissement :", arrondissement)
        data = ", Montreal, CANADA"
        data = arrondissement + data
        g = ox.graph_from_place(data, network_type="drive")
        G = nx.Graph(g)
        print("--- Eulerization du quartier ", arrondissement, " ---")
        g_eulerize = nx.eulerize(G)
        print("--- Fin Eulerization ---")
        print("---Debut de Eulerian circuit---")
        res = list(nx.eulerian_circuit(g_eulerize))
        print("---Fin de Eulerian circuit---")
        circuits.append(res)
    return circuits

circuits = chemin_drone()

print("--- List des circuits ---")
print(circuits)

print(time.localtime(time.time()))
