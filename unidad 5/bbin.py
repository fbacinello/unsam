def busqueda_binaria(lista, x, verbose=False):
    """Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def donde_insertar(lista, x):
    """Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio

        if lista[medio] == x:
            return medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda

    if izq == len(lista):  # si es mas grande que todos los elementos
        return len(lista)

    return pos


# print(donde_insertar([0, 2, 4, 6], -1))
# print(donde_insertar([0, 2, 4, 6, 11, 14, 22, 43], 42))
# print(donde_insertar([0, 2, 4, 6, 11, 14, 22, 43], 44))


def insertar(lista, x):
    resultado_busqueda = busqueda_binaria(lista, x)
    if resultado_busqueda == -1:
        pos = donde_insertar(lista, x)
        new = list(lista[:pos])
        new.append(x)
        new += lista[pos:]
        return pos, new
    else:
        return resultado_busqueda


lista1 = [0, 2, 4, 6, 11, 14, 22, 43]

posi, new1 = insertar([0, 2, 4, 6, 11, 14, 22, 43], 42)
print(posi)
print(new1)
