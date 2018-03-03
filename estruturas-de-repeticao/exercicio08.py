numero = int(input("Digite um numero: "))

quantDivisores = 0 

for contador in range(1,numero+1):       

   if (numero % contador) == 0:              

       quantDivisores += 1

if quantDivisores == 2:      

   print(numero,"eh primo.") 

else:       

   print(numero,"nao eh primo.")

