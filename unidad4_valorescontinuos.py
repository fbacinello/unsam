# Ejercicio 4.6: Calcular pi
import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x, y


def estimar_pi(n, m):
    return 4*m/n


N = 100000
M = sum([(x ** 2 + y ** 2) < 1 for x, y in
         [generar_punto() for i in range(N)]])
print('Pi:', estimar_pi(N, M))



