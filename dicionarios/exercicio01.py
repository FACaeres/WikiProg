carro = {"fabricante": "", "modelo": "", "ano": 0,"cor": "", "preco": 0}
ano_atual = 0

carro["fabricante"] = input("Qual o fabricante: ")
carro["modelo"] = input("Qual o modelo: ")
carro["ano"] = int(input("Qual o ano do carro: "))
carro["cor"] = input("Qual a cor: ")
carro["preco"] = float(input("Qual o preco: "))
ano_atual = int(input("\nQual o ano atual: "))

if (carro["ano"] == ano_atual):
   print("NOVO")
elif (carro["ano"] > (ano_atual - 4)):
   print("SEMINOVO")
else:
   print("VELHO")
