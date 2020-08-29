# Ejercicio 4.5: Envido
import random
from collections import namedtuple
from itertools import groupby
from operator import itemgetter

Carta = namedtuple('Carta', 'palo valor')

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [Carta(palo, valor) for valor in valores for palo in palos]

puntajes = {
    1: 11,
    2: 12,
    3: 13,
    4: 14,
    5: 15,
    6: 16,
    7: 17,
    10: 10,
    11: 10,
    12: 10
}

def calcular_puntos(tirada):
    grupo = groupby(tirada, itemgetter(0))
    grupos = [[item for item in data] for (key, data) in grupo]
    cartas_mismo_palo = [grupo for grupo in grupos if len(grupo) > 1]

    if len(cartas_mismo_palo) >= 1:
        if len(cartas_mismo_palo[0]) >= 2:
            cartas_puntaje = [puntajes[carta.valor] for carta in cartas_mismo_palo[0]]
            ordenados = sorted(cartas_puntaje, reverse=True)[0:2]
            return sum(ordenados)
    else:
        return 0


def repartir():
    return random.sample(naipes, 3)


N = 1000000

G = [calcular_puntos(repartir()) for i in range(N)]

cant_31 = sum([puntos == 31 for puntos in G])
cant_32 = sum([puntos == 32 for puntos in G])
cant_33 = sum([puntos == 33 for puntos in G])

print(cant_31, 'de', N, 'intentos, dieron 31')
print(cant_32, 'de', N, 'intentos, dieron 32')
print(cant_33, 'de', N, 'intentos, dieron 33')





