a = int(input())

b = int(input()) 

c = int(input()) 

print("Numeros em ordem crescente: ")

if (a < b) and (a < c): 

   if (c > b): print(a, " ", b, " ", c) 

   else: print(a, " ", c, " ", b) 

elif (b < a) and (b < c): 

   if (c < a): print(b, " ", c, " ", a) 

   else: print(b, " ", a, " ", c) 

else: 

   if (a < b): print(c, " ", a, " ", b) 

   else: print(c, " ", b, " ", a)

