# Resolucao

""" Loja de tintas """

from math import ceil

""" Constantes - Inicio """

taxa_cobertura = 3 

capacidade_lata = 18 

custo_lata = 80.0 

""" Constantes - Fim """

area_total = float(input("Qual o tamanho da area (m2):")) 

quantidade_litros = area_total/taxa_cobertura 

quantidade_latas = (area_total/taxa_cobertura)/capacidade_lata 

quantidade_latas = ceil(quantidade_latas) 

custo_total = quantidade_latas * custo_lata

print("Quantidade de latas:", quantidade_latas) 

print("Valor: %.2f" %custo_total)
