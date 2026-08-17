def imprimir(lista):
    for i in range(0, len(lista), 1):
        print(i + 1, "-", lista[i])


lista = [1, "Gato", 3.5, True]

imprimir(lista)