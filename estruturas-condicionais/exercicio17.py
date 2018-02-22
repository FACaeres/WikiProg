num1, num2, num3, num4, num5 = map(int, input().split())

soma = num1 + num2 + num3 + num4 + num5 

produto = num1 * num2 * num3 * num4 * num5 

if (soma % 2 == 0): 

   print("A soma %d eh par." %soma) 

else: 

   print("A soma %d eh impar." %soma) 

if (produto % 2 == 0): 

   print("O produto %d eh par." %produto) 

else: 

   print("O produto %d eh impar." %produto) 
