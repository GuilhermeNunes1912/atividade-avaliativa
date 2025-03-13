#Limpar terminal
import os 
os.system("clear")

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: "))

match sexo:
    case "f":
        estado_civil = str (input("Digite seu estado civil: ")).lower()
        if estado_civil == "casada":
            ano = int(input("Digite o ano de casados: "))
            print(f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome} Estado civil Solteira(O)")
    case "m":
        estado_civil = str(input("Digite seu estado civil: ")).lower()
        if estado_civil == "casado":
            ano = int(input("Digite o ano de casados: "))
            print(f"{nome} do sexo {sexo} e {estado_civil} a {ano} anos")
        else:
            print(f"{nome}estado civil Solteira(O)")
    case _:
        print("Algo esta errado")