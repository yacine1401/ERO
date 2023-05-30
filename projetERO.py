import osmnx as ox

city = ox.graph_from_place("Montreal, CANADA", network_type="drive")
print(city)
ox.plot_graph(city, node_color="r")

