"""Guarda em variaveis os valores das taxas""" 

taxaFixa = 26.89 

taxa0a5 = 1.41 

taxa5a10 = 5.29 

taxaAcima10 = 9.98

"""Obtem do usuario o consumo""" 

consumo = int(input())

"""Considera, a principio que conta tem o valor da taxa fixa""" 

conta = taxaFixa

"""Trata o caso do consumo acima de 10. Calcula a taxa do que execedeu a 10 e guarda na variavel consumo o que falta considerar""" 

if consumo > 10: 

   conta = conta + (consumo - 10)*taxaAcima10 

   consumo = 10

"""Trata a faixa de consumo de 5 a 10""" 

if consumo > 5: 

   conta = conta + (consumo - 5)*taxa5a10 

   consumo = 5

"""Trata a faixa de consumo de 0 a 5""" 

conta = conta + consumo*taxa0a5

"""Exibe o valor da conta""" 

print(conta)
