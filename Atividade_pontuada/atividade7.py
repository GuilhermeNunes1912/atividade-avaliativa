import os

os.system("clear") # Limpa o Terminal.

nome_produto = str(input("Digite a descriçao do produto: "))
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitario: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade >5 and quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

total_final = total - desconto

print(f"total:  R${total:.2f}")
print(f"Desconto:  R${desconto:.2f}")
print(f"Total a pagar:  R${total_final:.2f}")