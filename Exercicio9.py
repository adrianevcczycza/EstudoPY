def linhas(tamanho):
    for i in range(1, tamanho + 1, 1):
        print("_", end="")

tamanho = int(input("Insira o tamanho da sua linha: "))
linhas(tamanho)