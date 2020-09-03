# Ejercicio 4.7
import random

MU = 37.5
SIGMA = 0.2
N = 99

temperaturas = [random.normalvariate(MU, SIGMA)
                for i in range(N)]

print('Valor maximo:', max(temperaturas))
print('Valor minimo:', min(temperaturas))
print('Valor promedio:', sum(temperaturas)/N)
temperaturas.sort()
print('Mediana:', temperaturas[round(N/2)])


# Ejercicio 4.9
import numpy as np

N = 999

temperaturas = [random.normalvariate(MU, SIGMA)
                for i in range(N)]

temperaturas_array = np.array(temperaturas)
np.save('./Data/Temperaturas', temperaturas_array)
