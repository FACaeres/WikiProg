"""Programa que calcula o consumo de um automovel"""

distancia = float(input("Qual a distancia percorrida (Km)? ")) 

litros = float(input("Qual a quantidade de combustivel consumida (l)? ")) 

consumo = distancia / litros 

if consumo < 8: 

   print("Venda o carro!") 

elif (consumo >= 8) and (consumo <= 14): 

   print("Economico!") 

else: 

   print("Super economico!")
