import random
import numpy as np

def crear_album(cant_figus_album):
    return np.zeros(cant_figus_album)

def album_incompleto(album):
    return not np.all(album >= 1)

def comprar_figu(cant_figus_album):
    return random.randint(0, cant_figus_album -1)

def cuantas_figus(cant_figus_album):
    contador = 0
    album = crear_album(cant_figus_album)
    while album_incompleto(album):
        nueva_figu = comprar_figu(cant_figus_album)
        album[nueva_figu] += 1
        contador += 1

    return contador

# Ejercicio 4.15
N = 1000
tamaño_album = 6

cant_figus_para_llenar = [cuantas_figus(tamaño_album)
                          for i in range(N)]
print('En promedio se necesitaron', np.mean(cant_figus_para_llenar), 'para llenar el album')

# Ejercicio 4.16

N = 1000
tamaño_album = 670

cant_figus_para_llenar = [cuantas_figus(tamaño_album)
                          for i in range(N)]
print('En promedio se necesitaron', np.mean(cant_figus_para_llenar), 'para llenar el album')

# Ejercicio 4.17 y 4.18

def comprar_paquete(cant_figus_album, cant_por_paquete):
    return [random.randint(0, cant_figus_album -1) for i in range(cant_por_paquete)]

# Ejercicio 4.19

def cuantas_figus(cant_figus_album, tamaño_paquete):
    contador = 0
    album = crear_album(cant_figus_album)
    while album_incompleto(album):
        nuevo_paquete = comprar_paquete(cant_figus_album, tamaño_paquete)
        for figu in nuevo_paquete:
            album[figu] += 1
        contador += 1

    return contador

# Ejercicio 4.20  *.*

N = 100
tamaño_album = 670
tamaño_paquete = 5

cant_paquetes = [cuantas_figus(tamaño_album, tamaño_paquete) for i in range(N)]
print('Cant paquetes en promedio', np.mean(cant_paquetes))

# Ejercicio 4.21

bool_850 = [cant <= 850 for cant in cant_paquetes]
print('Probabilidad de llenarlo con 850 paquetes o menos: ', (np.sum(bool_850)/N)*100, '%')

# Ejercicio 4.22

import matplotlib.pyplot as plt

plt.hist(cant_paquetes, bins=20)
plt.show()
