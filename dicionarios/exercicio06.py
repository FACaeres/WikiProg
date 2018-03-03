"""Resolução""".

def encontrarPosicao(planetas,busca):

   pos = -1 

   cont = 0 

   while cont < len(planetas) and pos == -1: 

       if planetas[cont]["planeta"] == busca: 

           pos = cont 

       cont += 1 

   return pos

def principal():

   n = int(input()) 

   storms = [] 

   planetas = []

   for i in range(n): 

       storms.append({}) 

       storms[i]["nome"] = input()

       storms[i]["origem"] = input() 

       storms[i]["batalhas"] = int(input()) 

       indiceInsercao = encontrarPosicao(planetas,storms[i]["origem"]) 

       if  indiceInsercao == -1: 

           novo = {"planeta": storms[i]["origem"], "quantidade": 1} 

           planetas.append(novo) 

       else: 

           planetas[indiceInsercao]["quantidade"] += 1

   for i in range(len(planetas)): 

       print(planetas[i]["planeta"] + ":", planetas[i]["quantidade"]) 

principal()

