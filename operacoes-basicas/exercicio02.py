# Resolucao

quantidade_salario_hora = float(input("Quanto voce ganha por hora: ")) 

quantidade_horas = int(input("Quantas horas voce trabalhou este mes: "))

salario_bruto = quantidade_salario_hora * quantidade_horas 

salario_liquido = salario_bruto 

imposto_renda = 0.11 * salario_liquido 

salario_liquido = salario_liquido - imposto_renda 

imposto_inss = 0.08 * salario_bruto 

salario_liquido = salario_liquido - imposto_inss 

imposto_sindicato = 0.05 * salario_bruto 

salario_liquido = salario_liquido - imposto_sindicato

print("Salario bruto:",salario_bruto) 

print("Imposto renda:",imposto_renda) 

print("INSS:",imposto_inss) 

print("Sindicato:",imposto_sindicato) 

print("Salario liquido:",salario_liquido)
