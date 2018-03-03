"""Resolução""".

def iguais(A,B,quant): 

   iguais = True 

   contA = len(A)-1-quant 

   contB = 0 

   while contA < len(A) and iguais: 

       if A[contA] != B[contB]: 

           iguais = False 

       contA += 1 

       contB += 1 

   return iguais 

def condensar(A, B): 

   contA = 0 

   quant = -1 

   while contA < len(A): 

       tentativa = iguais(A,B,contA) 

       if tentativa: 

           quant = contA 

       contA += 1

   if quant != -1: 

           saida = A 

           for i in range(quant+1,len(B)): 

               saida += B[i] 

           return saida 

   else: 

           return "impossivel" 

def principal():   

   palavra1, palavra2 = input().split()   

   print(condensar(palavra1,palavra2))

principal()
