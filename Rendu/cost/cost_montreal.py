# arguments :
# - road --> tableau contenant les distances a parcourir en km
# - nb_v1 ---> nombre de vehicule de type I
# - nb_v2 ---> nombre de vehicule de type II
# return :
# - prix en euro du parcours de deneigeage
import time

start = time.time()
def cost(road, nb_v1, nb_v2):
    size_road = sum(road)
    portion_road_v1 = size_road / (nb_v1 + 2 * nb_v2)
    portion_road_v2 = portion_road_v1 * 2
    cost = nb_v1 * 500 + nb_v2 * 800
    n = 0
    hours = 0
    for j in range(nb_v1):
        road_vehicule = 0
        while (road_vehicule < portion_road_v1) and (n < len(road)):
            road_vehicule += road[n]
            n += 1
        hours = max(road_vehicule / 10, hours)
        cost += (road_vehicule * 1.1)
        if (road_vehicule / 10 > 8):
            cost += ((road_vehicule / 10 - 8) * 1.3)
            road_vehicule = 80
        cost += ((road_vehicule / 10) * 1.1)
    for k in range(nb_v2):
        road_vehicule = 0
        while (road_vehicule < portion_road_v2) and (n < len(road)):
            road_vehicule += road[n]
            n += 1
        hours = max(road_vehicule / 20, hours)
        cost += (road_vehicule * 1.3)
        if (road_vehicule / 20 > 8):
            cost += ((road_vehicule / 20 - 8) * 1.5)
            road_vehicule = 160
        cost += ((road_vehicule / 20) * 1.3)
    return cost, hours


# test
r = [10, 23, 16, 17, 54, 23, 76, 47, 32]
print("calcul a la main = ", end="")
print(500 + sum(r) * 1.1 + (sum(r) / 10 - 8) * 1.3 + 8 * 1.1)

print("calcul a l'aide de la fct = ", end="")
print(cost(r, 1, 0))


# Resultat

from tsp import tsp_quartier
import osmnx as ox
import networkx as nx
import math

lengths = []
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

def add_lengths(nom):
    quartier = tsp_quartier(nom)

    quartier_edges = [(quartier[i], quartier[i+1]) for i in range(len(quartier) - 1)]

    data = ", Montreal, CANADA"
    data = nom + data
    g = ox.graph_from_place(data, network_type="drive")
    G = g.to_undirected()

    edges = list(G.edges(keys=True, data=True))
    for quartier_edge in quartier_edges:
        for edge in edges:
            if quartier_edge == (edge[0], edge[1]):
                lengths.append(edge[3]['length'] / 1000)

for nom in arrondissements:
    add_lengths(nom)

for nb_v1 in range(10):
    for nb_v2 in range(10): 
        cout = cost(lengths, nb_v1, nb_v2)
        print(f"Cout pour {nb_v1} v1 et {nb_v2} v2:", round(cout[0], 2), "euros,", math.floor(cout[1]), "heures", math.ceil((cout[1] - math.floor(cout[1])) * 60), "minutes")
        print("===================================")

print("Total length=", sum(lengths) * 1000, "metres")
end = time.time()
elapsed = end - start
print(f'Temps d\'éxécution : {elapsed:.2}s')
