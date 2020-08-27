import random
from collections import namedtuple
from itertools import groupby
from operator import itemgetter

Carta = namedtuple('Carta', 'Palo Valor')

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [Carta(palo, valor) for valor in valores for palo in palos]




tirada = random.sample(naipes, 3)
print(tirada)

grupo = groupby(tirada, itemgetter(0))
grupos = [[item for item in data] for (key, data) in grupo]
print(grupos)




