import os

os.system("clear") # Limpa o Terminal.

cor = input("Digite a cor do CD: ")

if cor == "Vermelho":
    preco = 40,00
elif cor == "Azul":
    preco = 20,00
elif cor == "Verde":
    preco = 30,00
elif cor == "Aamarelo":
    preco = 10,00
else:
    print("Cor invalida!!")

print(f" A cor do CD e {cor} e o preco e {preco}")