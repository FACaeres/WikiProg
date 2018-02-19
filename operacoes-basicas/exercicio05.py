# Resolucao

"""Problema: Calcular a altura do aviao apos percorrer X metros formando angulo de 30º com o solo."""

"""importando comandos sin e radians do modulo math"""

from math import sin 

from math import radians

"""Entradas: um número real X"""

x = float(input("Informe o valor de x: "))

"""Processamento:"""

"""Qual a propriedade trigonometrica que nos permite calcular a altura?"""

"""seno(angulo) = cateto oposto / hipotenusa"""

"""seno(30) = altura / x""" 

"""altura = x * seno(30)""" 

angulo_rad = radians(30) 

altura = x * sin(angulo_rad)

"""Saidas: exibir altura""" 

print("A altura atingida eh:", altura)
