"""Resolução""".

def somar_digitos(num): 

   num = str(num) 

   soma = 0 

   for i in range(len(num)): 

       soma += int(num[i]) 

   return soma 

def harshad(num): 

   soma = somar_digitos(num) 

   if num % soma == 0: 

       return True 

   return False 

def principal(): 

   numero = int(input()) 

   print(harshad(numero))

principal()
