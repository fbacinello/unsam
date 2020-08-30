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

#Ejercicio 4.7: Gaussiana
import matplotlib.pyplot as plt


temperatura = 37.5
MU = 0
SIGMA = 0.2
N = 9999

temperaturas = [random.normalvariate(MU, SIGMA) + temperatura
                for i in range(N)]

print('Valor maximo:', max(temperaturas))
print('Valor minimo:', min(temperaturas))
print('Valor promedio:', sum(temperaturas)/N)

# plt.plot(temperaturas)
plt.hist(temperaturas, bins=200)
plt.show()