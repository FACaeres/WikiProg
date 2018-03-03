"""Resolução""".

qtde_valores = int(input()) valor = float(input())

menor_valor = valor

valores_lidos = 1 

while valores_lidos < qtde_valores: 

   valor = float(input()) 

   valores_lidos += 1 

   if valor < menor_valor: 

       menor_valor = valor

print(menorValor)

