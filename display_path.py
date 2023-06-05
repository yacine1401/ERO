import osmnx as ox
import networkx as nx
import math
import time
import matplotlib.pyplot as plt
import networkx.algorithms.approximation as nx_app

named_tuple = time.localtime() # get struct_time
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

tsp = nx.approximation.traveling_salesman_problem
def tsp_quartier(nom):
    circuits = []
    print("Arrondissement :", nom)
    data = ", Montreal, CANADA"
    data = nom + data
    g = ox.graph_from_place(data, network_type="drive")
    G = nx.Graph(g)
    print("--- Eulerization du quartier ", nom, " ---")
    g_eulerize = nx.eulerize(G)
    print("--- Fin Eulerization ---")
    # christo = nx_app.christofides(g_eulerize, weight="weight")
    sol = tsp(G, cycle=False)

    print(sol)
    #nx.draw(G)
    #plt.show()
    routes = []
    for i in range(len(sol) - 1):
        route = nx.shortest_path(G, sol[i], sol[i + 1])
        routes.append(route)
        fig, ax = ox.plot_graph_route(G, route, node_size=0,edge_color='grey', bgcolor='white')

    return sol

#circuits = chemin_drone()
quartier = tsp_quartier("Outremont")



print("--- List des circuits ---")
#print(quartier)


#cycle = quartier
#edge_list = list(nx.utils.pairwise(cycle))
#nx.draw_networkx_edges(H, pos, edge_color="blue", width=0.5)



