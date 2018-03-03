lista = list(map(float,input().split()))
soma = 0
for cont in range(len(lista)):
   soma += lista[cont]

media = soma/len(lista)
for cont in range(len(lista)):
   if lista[cont] > media:
       print(lista[cont],cont+1)
