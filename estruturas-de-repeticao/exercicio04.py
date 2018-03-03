deposito = float(input("Deposito inicial: "))

juros = float(input("Rendimento mensal: "))

mes = 1

valorAcumulado = deposito

while mes <= 12:

   valorAcumulado = valorAcumulado + valorAcumulado*juros

   print("No mes",mes,"o saldo e: %.2f" %valorAcumulado)

   mes = mes+1

print("Ao final de um ano o saldo e: %.2f" %valorAcumulado)

