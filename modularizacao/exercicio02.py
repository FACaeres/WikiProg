def fat(N):
   resultado = 1
   for cont in range(N,1,-1):
       resultado *= cont
   return resultado

def expressaoE(N):
   resposta = 1
   for cont in range(2,N+1):
       resposta = resposta + 1/fat(cont-1)
   return resposta

num = int(input())
print(expressaoE(num))
