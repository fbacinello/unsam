import libreria_arboles

path_archivo = './Data/arbolado-en-espacios-verdes.csv'
parque_gralpaz = 'GENERAL PAZ'

lista_arboles_gralpaz = libreria_arboles.leer_parque(path_archivo, parque_gralpaz)
print('Cantidad de arboles en el parque', parque_gralpaz, ':', len(lista_arboles_gralpaz))

especies_gralpaz = libreria_arboles.especies(lista_arboles_gralpaz)
print('Cantidad de especies en el parque', parque_gralpaz, ':', len(especies_gralpaz))
print('Lista de especies en el parque', parque_gralpaz, ':', especies_gralpaz)

print('Especies mas comunes en', parque_gralpaz, libreria_arboles.mas_comun(lista_arboles_gralpaz))

parque_losandes = 'ANDES, LOS'
lista_arboles_losandes = libreria_arboles.leer_parque(path_archivo, parque_losandes)
print('Especies mas comunes en', parque_losandes, libreria_arboles.mas_comun(lista_arboles_losandes))

parque_centenario = 'CENTENARIO'
lista_arboles_centenario = libreria_arboles.leer_parque(path_archivo, parque_centenario)
print('Especies mas comunes en', parque_centenario, libreria_arboles.mas_comun(lista_arboles_centenario))

especie_arbol = 'Jacarandá'
alturas_gralpaz = libreria_arboles.obtener_alturas(lista_arboles_gralpaz, especie_arbol)
print('En el parque', parque_gralpaz, 'el', especie_arbol, 'mas alto mide', max(alturas_gralpaz),
      'y en promedio miden', sum(alturas_gralpaz)/len(alturas_gralpaz))

alturas_losandes = libreria_arboles.obtener_alturas(lista_arboles_losandes, especie_arbol)
print('En el parque', parque_losandes, 'el', especie_arbol, 'mas alto mide', max(alturas_losandes),
      'y en promedio miden', sum(alturas_losandes)/len(alturas_losandes))

alturas_centenario = libreria_arboles.obtener_alturas(lista_arboles_centenario, especie_arbol)
print('En el parque', parque_centenario, 'el', especie_arbol, 'mas alto mide', max(alturas_centenario),
      'y en promedio miden', sum(alturas_centenario)/len(alturas_centenario))
