import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # ciclo cerrado opcional
    return total

def simulated_annealing(ruta, coord, T, T_MIN, V_enfriamiento):
    while T > T_MIN:
        dist_actual = evalua_ruta(ruta, coord)
        for _ in range(V_enfriamiento):
            i, j = random.sample(range(1, len(ruta)-1), 2)  # evita origen/destino
            ruta_tmp = ruta[:]
            ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
            dist_nueva = evalua_ruta(ruta_tmp, coord)
            delta = dist_actual - dist_nueva
            if dist_nueva < dist_actual or random.random() < math.exp(delta / T):
                ruta = ruta_tmp
                break
        T -= 0.005
    return ruta
