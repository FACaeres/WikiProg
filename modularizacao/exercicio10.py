"""Resolução""".

def fatorial(a): 

   fat = 1 

   for i in range(a,1,-1):

       fat *= i 

   return fat

def fibonacci(a): 

   fib, f_1, f_2 = 0, 0, 0 

   for i in range(1,a+1):

       if i == 1: 

           fib = 1 

      elif i == 2: 

          fib = 1 

           f_1, f_2 = 1, 1 

       else: 

           fib = f_1 + f_2 

           f_2 = f_1 

           f_1 = fib 

   return fib

def operacao(a,b): 

   if a == "fatorial": 

       return fatorial(b) 

   elif a == "fibonacci": 

       return fibonacci(b) 

   else: 

       return -1

def principal(): 

   numero = int(input()) 

   op = input()

    res = operacao(op,numero) 

   if res != -1: 

       print(res)

principal()

