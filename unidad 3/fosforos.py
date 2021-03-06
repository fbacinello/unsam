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
                    break
                else:
                    continue

            for n in range(0, i, -1):
                if fosforos[i - n] == 0:
                    fosforos[n] = 1
                if fosforos[n] == -1:
                    break
                else:
                    continue

    return fosforos


fosforos = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
fosforos_test = [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# print(propagar_str(fosforos))
resultado = propagar(fosforos)

print(resultado)
# assert resultado == fosforos_test, 'Todo mal'
if resultado == fosforos_test:
    print('Salio bien papu')
else:
    print('Cagaste fuego')


fosforos = [1, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0,-1, -1, 0, 0, 1, 1, 1, -1, 0, 1, -1, 0]
fosforos_test = [1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 0]

resultado = propagar(fosforos)
print(resultado)
# assert resultado == fosforos_test, 'Todo mal'
if resultado == fosforos_test:
    print('Salio bien papu2')
else:
    print('Cagaste fuego2')

def propagar2(fosforos):
    for i, e in enumerate(fosforos):
        if e == 1:
            # propago adelante
            a = i
            while True:
                a += 1
                if not a >= len(fosforos):
                    if fosforos[a] == 0:
                        fosforos[a] = 1
                    if fosforos[a] == -1:
                        break
                else:
                    break

            # propago atras
            b = i
            while True:
                b -= 1
                if b >= 0:
                    if fosforos[b] == 0:
                        fosforos[b] = 1
                    if fosforos[b] == -1:
                        break
                else:
                    break
    return fosforos


fosforos = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
fosforos_test = [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# print(propagar_str(fosforos))
resultado = propagar2(fosforos)

print(resultado)
# assert resultado == fosforos_test, 'To do mal'
if resultado == fosforos_test:
    print('Salio bien papu')
else:
    print('Cagaste fuego')


fosforos = [1, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0, -1, -1, 0, 0, 1, 1, 1, -1, 0, 1, -1, 0]
fosforos_test = [1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 0]

resultado = propagar2(fosforos)
print(resultado)
# assert resultado == fosforos_test, 'To do mal'
if resultado == fosforos_test:
    print('Salio bien papu2')
else:
    print('Cagaste fuego2')
