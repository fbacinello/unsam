# Ejercicio 4.3 Generala servida
import random
from collections import Counter


def tirar(cant_dados=5):
    return [random.randint(1, 6) for i in range(cant_dados)]


def es_generala(tirada):
    return len(set(tirada)) == 1

N = 100000

# G = sum([es_generala(tirar()) for i in range(N)])
# print('De', N, 'intentos,', G, 'salieron generala.')

# Ejercicio 4.4 - Generala no necesariamente servida
def contar(tirada):
    return Counter(tirada)


def cual_salio_mas(contador):
    return contador.most_common(1)[0]


def buscar_dado(tirada, dado):
    contador = dict(Counter(tirada))
    if dado in contador.keys():
        return contador[dado]
    else:
        return 0


def generala():
    tirada = tirar()
    print(tirada)

    contador = contar(tirada)
    print(contador)

    dado_elegido, cant = cual_salio_mas(contador)
    print('El dado', dado_elegido, 'salio', cant, 'veces')

    tiradas = 1
    while tiradas < 3:
        tiradas += 1
        print('----------------')
        tirada = tirar(5 - cant)
        print(tirada)
        cant += buscar_dado(tirada, dado_elegido)
        print(cant)

        if cant == 5:
            print('GENERALA')
            break

    return cant == 5

N = 1000

# G = sum([generala() for i in range(N)])
# print('De', N, 'veces,', G, 'salieron generala')

