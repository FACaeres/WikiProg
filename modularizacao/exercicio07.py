"""Resolução""".

def eh_vogal(letra): 

   vogais = "aeiou" 

   for i in range(len(vogais)): 

       if letra == vogais[i]: 

           return True 

   return False

def contar_vogais(palavra): 

   nro_vogais = 0 

   for i in range(len(palavra)): 

       if eh_vogal(palavra[i]): 

           nro_vogais += 1 

   return nro_vogais

def principal(): 

   palavra = input() 

   print(contar_vogais(palavra))

principal()

