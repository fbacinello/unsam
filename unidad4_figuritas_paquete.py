import random
import numpy as np

def crear_album(cant_figus_album):
    return np.zeros(cant_figus_album)


def album_incompleto(album):
    return not np.all(album >= 1)


def comprar_paquete(cant_figus_album, cant_por_paquete):
    return [random.randint(0, cant_figus_album -1) for i in range(cant_por_paquete)]


def cuantas_figus(cant_figus_album, tamaño_paquete):
    contador = 0
    album = crear_album(cant_figus_album)
    while album_incompleto(album):
        nuevo_paquete = comprar_paquete(cant_figus_album, tamaño_paquete)
        for figu in nuevo_paquete:
            album[figu] += 1
        contador += 1

    return contador, album


tamaño_album = 670
tamaño_paquete = 5
cant_paquetes_para_llenar, album = cuantas_figus(tamaño_album, tamaño_paquete)
print('Se necesitaron', cant_paquetes_para_llenar, 'paquetes para llenar el album')
print('Se necesitaron', cant_paquetes_para_llenar * tamaño_paquete, 'figus para llenar el album')
print('La figu que mas veces se repitio fue', int(max(album)), 'veces')

N = 100

cant_paquetes = [cant_paquetes for cant_paquetes, album in
                 [cuantas_figus(tamaño_album, tamaño_paquete) for i in range(N)]]

print('Cant paquetes en promedio', np.mean(cant_paquetes))

