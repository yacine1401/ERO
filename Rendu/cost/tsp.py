import osmnx as ox
import networkx as nx
import math
import time
import sys
import matplotlib.pyplot as plt
import networkx.algorithms.approximation as nx_app

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string)

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

tsp = nx.approximation.traveling_salesman_problem

def tsp_quartier(nom):
    circuits = []
    print("Arrondissement:", nom)
    data = nom + ", Montreal, CANADA"
    g = ox.graph_from_place(data, network_type="drive")
    G = g.to_undirected()
    g_eulerize = nx.eulerize(G)

    # approximation de la sol avec TSP
    sol = tsp(g_eulerize, cycle=False)

    subgraph = G.subgraph(sol)
    paths = []
    for i, node in enumerate(sol[:-1]):
        #print(node)
        next_node = sol[i + 1]

        if G.has_edge(node, next_node):
            path = nx.shortest_path(subgraph, node, next_node, weight="length")
            if(len(path)==2):
                paths.append(path)
    print("--- Debut du TSP ---")
    fig, ax = ox.plot_graph(G,show=False,close=False, edge_color='grey') 

    for (u,v) in paths:
        x=[G.nodes[u]['x'],G.nodes[v]['x']]
        y= [G.nodes[u]['y'],G.nodes[v]['y']]
        ax.plot(x, y,'m', linewidth=2)
        plt.pause(0.05)

    print("--- Fin du TSP ---")

    #print(paths)
    return sol

quartier = tsp_quartier(sys.argv[1])
