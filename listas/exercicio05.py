lista = input().split()

for palavra in lista:
   if len(palavra) >= 5 and palavra[:2] == "in":
       print(palavra)
