def calcular_media(lista):
    soma = 0

    for i in range(0, len(lista), 1):
        soma = soma + lista[i]

    media = soma / len(lista)

    return media


lista = [10, 8, 7, 5]

print(calcular_media(lista))