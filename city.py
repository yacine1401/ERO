import osmnx as ox

city = ox.graph_from_place("Montreal, CANADA", network_type="drive")
#ox.plot_graph(city, node_color="r")
print(city)