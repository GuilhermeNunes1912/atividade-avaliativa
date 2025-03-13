import os 

os.system("clear") 

Algarismo_A = int(input("Digite o valor A: "))
Algarismo_B = int(input("Digite o valor B: "))
Algarismo_C = int(input("Digite o valor C: "))

soma = (Algarismo_A + Algarismo_B)

print()

print (f"Soma dos algarismo A e B: {soma}")

print()

if soma < Algarismo_C:
    print("A + B é menor que C")
else:
    print("A + B é maior que C")
