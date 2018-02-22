"""Pedindo o salario para o usuario"""

salario = int(input("Digite o salario: "))

"""Verificando no nivel de renda"""

if salario < 1500:

  print("Baixa renda")

elif salario <= 3000:

  print("Renda media")

else:

  print("Alta renda")
