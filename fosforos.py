def propagar(lista):
    j = 0
    for i in range(len(lista)):
        if lista[i] == -1:
            tramo = lista[j:i]
            print(tramo)
            if 1 in tramo:
                for q in range(len(tramo)):
                    tramo[q] = 1
            print(tramo)
            j = i + 1

    print(lista)

def propagar_str(lista):
    lista_str = [str(num) for num in lista]
    print(lista_str)
    todo_en_uno = ''
    for string in lista_str:
        todo_en_uno += string

    print(todo_en_uno.split('-1'))
    spliteado = todo_en_uno.split('-1')
    prendido_fuego = []
    for tramo in spliteado:
        if '1' in tramo:
            prendido_fuego.append(tramo.replace('0', '1'))
        else:
            prendido_fuego.append(tramo)
    print(prendido_fuego)

    lista_ints = []
    for tramo in prendido_fuego:
        for char in tramo:
            lista_ints.append(int(char))
        lista_ints.append(-1)
    return lista_ints[0:-1]


def propagar(fosforos):
    for i, e in enumerate(fosforos):
        if e == 1:
            for n in range(i, len(fosforos)):
                if fosforos[n] == 0:
                    fosforos[n] = 1
                if fosforos[n] == -1:
                    continue
                else:
                    continue

            for n in range(i, len(fosforos), -1):
                if fosforos[n] == 0:
                    fosforos[n] = 1
                if fosforos[n] == -1:
                    continue
                else:
                    continue

    return fosforos



fosforos = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
fosforos_test = [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# print(propagar_str(fosforos))
resultado = propagar(fosforos)

print(resultado)
if resultado == fosforos_test:
    print('Salio bien papu')
else:
    print('Cagaste fuego')


fosforos = [1, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0,-1, -1, 0, 0, 1, 1, 1, -1, 0, 1, -1, 0]
fosforos_test = [1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1,-1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 0]

resultado = propagar(fosforos)
print(resultado)
if resultado == fosforos_test:
    print('Salio bien papu2')
else:
    print('Cagaste fuego2')