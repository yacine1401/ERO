# arguments :
# - road --> tableau contenant les distances a parcourir en km
# - nb_v1 ---> nombre de vehicule de type I
# - nb_v2 ---> nombre de vehicule de type II
# return :
# - prix en euro du parcours de deneigeage

def cost(road, nb_v1, nb_v2):
    size_road = sum(road)
    portion_road_v1 = size_road / (nb_v1 + 2 * nb_v2)
    portion_road_v2 = portion_road_v1 * 2
    cost = nb_v1 * 500 + nb_v2 * 800
    n = 0
    for j in range(nb_v1):
        road_vehicule = 0
        while (road_vehicule < portion_road_v1) and (n < len(road)):
            road_vehicule += road[n]
            n += 1
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
        cost += (road_vehicule * 1.3)
        if (road_vehicule / 20 > 8):
            cost += ((road_vehicule / 20 - 8) * 1.5)
            road_vehicule = 160
        cost += ((road_vehicule / 20) * 1.3)
    return cost


# test
r = [10, 23, 16, 17, 54, 23, 76, 47, 32]
print("calcul a la main = ", end="")
print(500 + sum(r) * 1.1 + (sum(r) / 10 - 8) * 1.3 + 8 * 1.1)

print("calcul a l'aide de la fct = ", end="")
print(cost(r, 1, 0))
