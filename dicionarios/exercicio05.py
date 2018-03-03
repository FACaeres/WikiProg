"""Resolução""".

def exibir_iguais(doadores,tipo): 

   for i in range(len(doadores)): 

       if doadores[i]["tipo"] == tipo: 

           print(doadores[i]["nome"])

def principal(): 

   n = int(input()) 

   doadores = [] 

   for i in range(n): 

       doadores.append({}) 

       doadores[i]["nome"] = input() 

       doadores[i]["tipo"] = input() 

   tipo_sanguineo = input() 

   exibir_iguais(doadores,tipo_sanguineo) 

   if tipo_sanguineo == "AB": 

       exibir_iguais(doadores,"A") 

       exibir_iguais(doadores,"B") 

   if tipo_sanguineo != "O": 

       exibir_iguais(doadores,"O")

principal()

