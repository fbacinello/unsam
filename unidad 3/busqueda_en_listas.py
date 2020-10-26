def buscar_u_elemento(lista, e):
    pos = -1
    for i, value in enumerate(lista):
        if value == e:
            pos = i
    return pos


print(buscar_u_elemento([1,2,3,2,3,4],1))
print(buscar_u_elemento([1,2,3,2,3,4],2))
print(buscar_u_elemento([1,2,3,2,3,4],3))
print(buscar_u_elemento([1,2,3,2,3,4],5))


def buscar_n_elemento(lista, e):
    cant = 0
    for value in lista:
        if value == e:
            cant += 1
    return cant


print(buscar_n_elemento([1,2,3,2,3,4],1))
print(buscar_n_elemento([1,2,3,2,3,4],2))
print(buscar_n_elemento([1,2,3,2,3,4],5))


def maximo(lista):
    max = lista[0]
    for e in lista:
        if e > max:
            max = e
    return max


print(maximo([1,2,7,2,3,4]))
print(maximo([1,2,3,4]))
print(maximo([-5,4]))
print(maximo([-5,-4]))


def busqueda_lineal(lista, e):
    """Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    """
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_lineal_ordenada(lista,e):
    """Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    Para cuando encuentra un valor mayor a e.
    """
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista):
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo.
        if z > e:
            break
    return pos
