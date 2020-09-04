# Ejercicio 5.3, 5.4 y 5.5
import csv


def parse_csv(nombre_archivo, select=None, types=None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(ncolumna) for ncolumna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            if types:
                fila = [func(val) for func, val in zip(types, fila)]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros


camion = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
print(camion)
