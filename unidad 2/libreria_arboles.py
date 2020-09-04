import csv
from collections import namedtuple
from collections import Counter


def leer_parque(path, parque=''):
    # tuve que pasarle ese encoding sino me llamaba
    file = open(path, 'rt', encoding='utf-8')
    reader = csv.reader(file, delimiter=',')

    # saco las columnas y creo los campos de mi namedtuple
    columns = next(reader)
    # para leer esto tenes que entender que es una namedtuple
    # pero pensalo como un diccionario, las columnas son las keys
    # y primero le pase 'Arbol' porque te pide que le pongas un nombre tambien, los diccionarios no
    Arbol = namedtuple('Arbol', columns)

    # genero una lista de namedtuple con todos los arboles
    # no vas a entender la forma en la que hago el for
    # esto es lo que queria practicar, es algo particular de python
    # se llama list comprehension
    # abajo te dejo escrito como seria con un for comun
    lista = [Arbol._make(row)
             for row in reader]

    # forma normal --------------------------------
    lista2 = []
    for row in reader:
        lista2.append(Arbol._make(row))
    # --------------------------------------------

    # filtro por parque
    # tambien list comprehension, tambien te hago la forma comun, pero mas adelante no lo hago mas jaja
    lista_parque = [arbol
                    for arbol in lista
                    if arbol.espacio_ve == parque]

    # forma normal ---------------------------------
    lista_parque2 = []
    for arbol in lista:
        if arbol.espacio_ve == parque:
            lista_parque2.append(arbol)
    # ----------------------------------------------

    # aca te dejo un temita para que pongas en spoty mirrrrey
    # https://open.spotify.com/track/1yjCz2WE7MvE9Pq0SNVqpQ?si=RXjvFWrTSB6IsEKCiNP0WQ
    return lista_parque


def especies(lista_arboles):
    # creo set
    return {arbol.nombre_com
            for arbol in lista_arboles}


def mas_comun(lista_arboles, cant=5):
    arboles_por_tipo = [arbol.nombre_com
                        for arbol in lista_arboles]
    counter = Counter(arboles_por_tipo)
    return counter.most_common(cant)


def obtener_alturas(lista_arboles, especie):
    return [float(arbol.altura_tot)
            for arbol in lista_arboles
            if arbol.nombre_com == especie]
