num1, num2, num3, num4, num5 = map(int, input().split())

soma = num1 + num2 + num3 + num4 + num5 

produto = num1 * num2 * num3 * num4 * num5 

if (soma % 2 == 0): 

   print(soma, "eh par.") 

else: 

   print(soma, "eh impar.") 

if (produto % 2 == 0): 

   print(produto, "eh par.") 

else: 

   print(produto, "eh impar.")
