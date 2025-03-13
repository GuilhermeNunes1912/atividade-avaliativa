# Limpar terminal
import os
os.system("clear")

print("""
==============================   MENU  ==============================
         FRUTAS      preço ate 5 kg     preço acima 5 kg 
 \t\t   maça            2,50                    2,20
 \t\t   morango         1,80                    1,50
=====================================================================
""")  

quant_morango = float(input("Diga a quantidade de morango: "))
quant_maça = float(input("Diga a quantidade de maças: "))

maça = float(2.50)
maça_2 = float(2.20)
morango = float(1.80)
morango_2 = float(1.50)


if quant_maça or quant_morango <=5:
    total=(quant_morango*morango)+(quant_maça*maça)
    print(f"Total: {total} ")
elif quant_maça or quant_morango > 8:
    total=(quant_morango*morango)+(quant_maça*maça)
    total_final=(total*0.10)
    print(f"Valor a ser pago:   {total_final} ")