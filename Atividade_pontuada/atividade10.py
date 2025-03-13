import os

os.system("clear") # Limpa o Terminal.

print("""
======================{Preço}======================
A = Alcool       3. 79R$
G = Gasolina       6. 59R$
""")

comb = input("Digite o tipo de combustivel deseja abastecer: ").upper()
litros = float(input("Digite a quantidade de litros que desejar abastecer: "))

os.system("clear")

if comb == "A":
    preço = 3.79
    tipo = "Alcool"
    
elif comb == "G":
    preço = 6.59
    tipo = "Gasolina"

match comb:
    case "A":
        if litros <= 25:
            desconto = preço * 0.02
        else:
            desconto = preço * 0.04
    case "g":
        if litros <= 25:
            desconto = preço * 0.3
        else:
            desconto = preço * 0.05
    case _:
        print("Combustivel nao encontrado")
        exit()

valor = preço * litros
valorfinal = valor - desconto
print(f"O valor total a ser pago e de R${valorfinal:.2f} no(a) {tipo}")
print(f"voce abasteceu {litros}L")