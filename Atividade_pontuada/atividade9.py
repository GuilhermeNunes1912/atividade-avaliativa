import os

os.system("clear") # Limpa o Terminal.

renda_mensal = float(input("Digite o valor da renda: "))
valor_emprestimo = float(input("Digite o valor do emprestimo: "))
num_prestacoes = float(input("Digite o numero das prestaçoes: "))

valor_prestaçao = (valor_emprestimo / num_prestacoes)

if valor_emprestimo <= 10 * renda_mensal and valor_prestaçao <= 0.30 * renda_mensal:
    print("Emprestimo autorizado! ")
else:
    print("Emprestimo nao autorizado! ")