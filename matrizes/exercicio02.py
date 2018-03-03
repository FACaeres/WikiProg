matriz = [0]*4
for i in range(len(matriz)):
   matriz[i] = [0] * 5
soma = [0]*5

for i in range(len(matriz)):
   for j in range(len(matriz[0])):
       matriz[i][j] = int(input())
       soma[j] += matriz[i][j]

print(soma)
 
