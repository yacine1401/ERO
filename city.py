import osmnx as ox

city = ox.graph_from_place("Montreal, CANADA", network_type="drive")