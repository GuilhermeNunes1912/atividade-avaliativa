import os

os.system("clear") # Limpa o Terminal.

nota_1 = float(input("Digite sua nota: "))
nota_2 = float(input("Digite sua nota: "))

total=(nota_1 + nota_2)

media=(total)/2

if media >=6:
    print("aprovado")

elif media <= 4:
    print("reprovado")