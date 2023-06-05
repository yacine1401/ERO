# G le graphe
# renvoie une liste de niveau de neige en centimetre
# pour chaque noeuds

import random as rd

def neige_gen(G):
    lvl_list = []
    for i in range(len(G.node)):
        lvl_list.append(rd.randint(0, 100))
    return lvl_list
