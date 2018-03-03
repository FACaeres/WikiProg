"""Resolução""".

def prob(rel,dist): 

   for i in range(dist): 

       rel = rel - 0.08*rel 

   return rel * 100 

def espaco(alvo): 

   total = len(alvo) 

   area = 0 

   for i in range(total): 

       if alvo[i] == "#": 

           area += 1 

   return area/total

def principal(): 

   dist = int(input()) 

   alvo = "" 

   linha = "" 

   while linha != "0": 

       linha = input() 

       if linha != "0": 

           alvo += linha 

   relEsp = espaco(alvo) 

   print(round(prob(relEsp,dist)))

principal()

