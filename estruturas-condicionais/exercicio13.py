time1 = input()

time2 = input()

vencedor_jogo1 = input()

vencedor_jogo2 = input()

vencedor_jogo3 = input()

vencedor_jogo4 = input()

vencedor_jogo5 = input()

vitorias_time1 = 0

vitorias_time2 = 0

if vencedor_jogo1 == "C":

   vitorias_time1 = vitorias_time1 + 1

else: 

   vitorias_time2 = vitorias_time2 + 1

if vencedor_jogo2 == "V": 

   vitorias_time1 = vitorias_time1 + 1 

else: 

   vitorias_time2 = vitorias_time2 + 1

if vencedor_jogo3 == "C": 

   vitorias_time1 = vitorias_time1 + 1 

else: 

   vitorias_time2 = vitorias_time2 + 1

if vencedor_jogo4 == "V": 

   vitorias_time1 = vitorias_time1 + 1 

else: 

   vitorias_time2 = vitorias_time2 + 1

if vencedor_jogo5 == "C": 

   vitorias_time1 = vitorias_time1 + 1 

else: 

   vitorias_time2 = vitorias_time2 + 1

if vitorias_time1 > vitorias_time2: 

   print(time1) 

else: 

   print(time2)
