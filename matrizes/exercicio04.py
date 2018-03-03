"""guarda o tamanho das matrizes"""
linhas = 3
colunas = 3

"""obtem a matriz A do usuario"""
matriz_A = [[]]*linhas
for i in range(linhas):
   matriz_A[i] = list(map(int, input().split()))

"""obtem a matriz B do usuario"""
matriz_B = [[]]*linhas
for i in range(linhas):
   matriz_B[i] = list(map(int, input().split()))

"""inicializa a matriz de soma"""
matriz_soma = [[]]*linhas
for i in range(linhas):
   matriz_soma[i] = [0]*linhas

"""preenche a matriz de soma"""
for i in range(linhas):
   for j in range(colunas):
       matriz_soma[i][j] = matriz_A[i][j] + matriz_B[i][j]

"""exibe a matriz de soma (na forma tabular)"""
for i in range(linhas):
   for j in range(colunas):
       print(matriz_soma[i][j], end="\t")
   print()
