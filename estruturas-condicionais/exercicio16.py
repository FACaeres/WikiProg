suspeito1 = input() 

suspeito2 = input() 

suspeito3 = input()

contador_sim = 0 

resposta = input() """resposta 1a. pergunta""" 

if resposta == "sim": 

   contador_sim += 1 

resposta = input() """resposta 2a. pergunta"""  

if resposta == "sim": 

   contador_sim += 1 

resposta = input() """resposta 3a. pergunta""" 

if resposta == "sim": 

   contador_sim += 1 

resposta = input() """resposta 4a. pergunta"""  

if resposta == "sim":

   contador_sim += 1 

resposta = input() """resposta 5a. pergunta"""  

if resposta == "sim": 

   contador_sim += 1

if contador_sim == 2: 

   print(suspeito1) 

elif 3 <= contador_sim <= 4: 

   print(suspeito2) 

elif contador_sim == 5: 

   print(suspeito3) 

else: 

   print(suspeito1,suspeito2,suspeito3)
