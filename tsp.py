import osmnx as ox
import networkx as nx
import math
import time
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
"""
def tsp_quartier(nom):
    circuits = []
    print("Arrondissement:", nom)
    data = nom + ", Montreal, CANADA"
    g = ox.graph_from_place(data, network_type="drive")
    #G = nx.Graph(g)
    G = g.to_undirected()
    print("--- Eulerization du quartier", nom, " ---")
    g_eulerize = nx.eulerize(G)
    print("--- Fin Eulerization ---")

    sol = tsp(G, cycle=False)
    ox.plot_graph(ox.graph_from_place(data, network_type="drive"), show=False)

    node_coords = nx.get_node_attributes(G, "x_y")
    node_coords = {k: node_coords[k] for k in sol if k in node_coords}
    subgraph = G.subgraph(sol)

    paths = []
    for i, node in enumerate(sol[:-1]):
        next_node = sol[i + 1]

        if G.has_edge(node, next_node):
            path = nx.shortest_path(subgraph, node, next_node, weight="length")
            paths.append(path)

            if node in node_coords:
                node_coord = node_coords[node]
                plt.plot(node_coord[0], node_coord[1], "ro", markersize=5)

    last_node = sol[-1]
    first_node = sol[0]

    if G.has_edge(last_node, first_node):
        path = nx.shortest_path(subgraph, last_node, first_node, weight="length")
        paths.append(path)

    ox.plot_graph(ox.graph_from_place(data, network_type="drive"), paths, node_size=0, edge_linewidth=2,
                        edge_color="blue", route_linewidth=4, show=False)
    

    if first_node in node_coords:
        node_coord = node_coords[first_node]
        plt.plot(node_coord[0], node_coord[1], "ro", markersize=5)

    plt.draw()
    plt.pause(0.5)
    plt.show()

    return sol

quartier = tsp_quartier("Outremont")


"""
def tsp_quartier(nom):
    circuits = []
    print("Arrondissement :", nom)
    data = ", Montreal, CANADA"
    data = nom + data
    g = ox.graph_from_place(data, network_type="drive")
    #G = nx.Graph(g)
    G = g.to_undirected()
    # christo = nx_app.christofides(g_eulerize, weight="weight")
    sol = tsp(G, cycle=False)

    #nx.draw(G)
    #plt.show()
    #for i in range(len(sol) - 1):
     # routes.append(nx.shortest_path(G, sol[i], sol[i + 1]))
    #fig , ax = ox.plot.plot_graph_route(G, sol, save=True, show=False, close=True )
    #fig , ax = ox.plot.plot_graph_route(G, sol, route_color='r', route_linewidth=4)

    #draw_networkx(sol)
    return sol



quartier = tsp_quartier("Outremont")

#print("--- List des circuits ---")
#print(quartier)

#cycle = quartier
#edge_list = list(nx.utils.pairwise(cycle))
#nx.draw_networkx_edges(H, pos, edge_color="blue", width=0.5)



