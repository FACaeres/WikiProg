"""Lendo o numero inteiro representando um binario""" 

binario = int(input())

"""Tratando o digito mais a direita (5o digito)""" 

decimal = binario % 2

"""Tratando o quarto digito"""

binario = binario // 10 

decimal = decimal + binario % 2 * 2**1

"""Tratando o terceiro digito""" 

binario = binario // 10 

decimal = decimal + binario % 2 * 2**2

"""Tratando o segundo digito""" 

binario = binario // 10 

decimal = decimal + binario % 2 * 2**3

"""Tratando o primeiro digito""" 

binario = binario // 10 

decimal = decimal + binario % 2 * 2**4

"""Exibindo decimal correspondente""" 

print(decimal)
