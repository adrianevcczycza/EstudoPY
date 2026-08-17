nota1 = int(input("Insira a nota 1: "))
nota2 = int(input("Insira a nota 2: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Em exame")
else:
    print("Reprovado")