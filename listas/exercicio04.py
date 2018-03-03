"""inicializa a lista com 8 elementos"""
lista=[0]*8

"""obtem um elemento por linha o usuario"""
for i in range(len(lista)):
   lista[i] = int(input())

"""exibe um elemento por linha (de traz pra frente)"""
for i in range(len(lista)-1, -1, -1):
   print(lista[i])
 
