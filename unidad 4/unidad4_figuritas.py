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

    return contador, album


tamaño_album = 670
cant_figus_para_llenar, album = cuantas_figus(tamaño_album)
print('Se necesitaron', cant_figus_para_llenar, 'para llenar el album')
print('La figu que mas veces se repitio fue', int(max(album)), 'veces')

