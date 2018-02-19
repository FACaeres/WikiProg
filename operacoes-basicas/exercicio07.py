# Resolucao

"""Importa a funcao teto (ceil) do modulo math""" 

from math import ceil

"""ENTRADAS: Solicita ao usuario o numero de paes e as quantidades de ingredientes""" 

nro_de_paes = int(input("Numero de paes: ")) 

print("Digite as quantidades para fazer 1 pao") 

qtde_farinha = float(input("Farinha: ")) 

qtde_fermento = float(input("Fermento: ")) 

qtde_sal = float(input("Sal: ")) 

qtde_acucar = float(input("Acucar: "))

"""PROCESSAMENTO: Calcula a quantidade de sacos de cada ingrediente para cada um calcula o total gasto para 

todos os paes e pega o teto da divisao pelo tamanho do saco em gramas"""

sacos_farinha = ceil((nro_de_paes * qtde_farinha ) / 10000) 

sacos_fermento = ceil((nro_de_paes * qtde_fermento) /   100) 

sacos_sal = ceil((nro_de_paes * qtde_sal ) /  1000) 

sacos_acucar = ceil((nro_de_paes * qtde_acucar ) /  5000)

"""SAIDAS: Exibe as quantidades de sacos necessarias print("Serao necessarios: ")"""

print("%-9s : %3d sacos" %("Farinha", sacos_farinha)) 

print("%-9s : %3d sacos" %("Fermento", sacos_fermento)) 

print("%-9s : %3d sacos" %("Sal", sacos_sal)) 

print("%-9s : %3d sacos" %("Acucar", sacos_acucar))
