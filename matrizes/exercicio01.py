numeros = [[0,0],[0,0]]

print("Informe os quatro elementos da matriz.")
print("Forneça um valor por linha.")
   for i in range(len(numeros)):
       for j in range(len(numeros[0])):
           numeros[i][j] = int(input())

determinante = numeros[0][0]*numeros[1][1]
determinante -= numeros[0][1]*numeros[1][0]

print("O determinante e: ",determinante)
 
