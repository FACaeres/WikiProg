numeros = [0] * 10 
PAR = [0] * 10
IMPAR = [0] * 10
cont = 0
contPAR = 0
contIMPAR = 0

while cont < len(numeros):      
   numeros[cont] = int(input())      
   if numeros[cont] % 2 == 0:              
       PAR[contPAR] = numeros[cont]              
       contPAR += 1      
   else:              
       IMPAR[contIMPAR] = numeros[cont]  
       contIMPAR += 1      
   cont += 1

cont = 0
print("ORIGINAL")
while cont < len(numeros):      
   print(numeros[cont],end=" ")      
   cont += 1

cont = 0
print("\nPAR")
while cont < contPAR:      
  print(PAR[cont],end=" ")
   cont += 1

cont = 0
print("\nIMPAR")
while cont < contIMPAR:      
   print(IMPAR[cont],end=" ")
   cont += 1 print("\n")
