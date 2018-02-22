from math import sqrt

a = float(input())

b = float(input())

c = float(input())

delta = b**2 - 4*a*c

if delta < 0:

   print("nao existem raizes")

else: 

   x1 = (-b + sqrt(delta)) / 2*a 

   if delta == 0: 

       print(x1) 

   else: 

       x2 = (-b - sqrt(delta)) / 2*a 

       print(x1, x2)
