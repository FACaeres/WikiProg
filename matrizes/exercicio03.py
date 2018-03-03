matriz = [0]*5
for i in range(len(matriz)):
   matriz[i] = [0]*5

for i in range(len(matriz)):
   matriz[i] = list(map(int,input().split()))

for i in range(len(matriz)):
   matriz[2][i], matriz[i][2] = matriz[i][2], matriz[2][i]

print("")
for i in range(len(matriz)):
   for j in range(len(matriz[0])):
       print(matriz[i][j], end = " ")
   print("")
