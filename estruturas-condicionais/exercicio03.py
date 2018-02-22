"""Emprestimo bancario para casa""" 

valor_casa = float(input("Insira o valor da casa (decimal): ")) 

valor_salario = float(input("Insira o valor do salario (decimal): ")) 

qtd_anos = int(input("Insira a quantidade de anos (inteiro): "))

prestacao_mensal = valor_casa / (qtd_anos*12) 

if prestacao_mensal > 0.3 * valor_salario: 

   print("Seu emprestimo foi negado!") 

else: 

   print("Seu emprestimo foi aceito!")
