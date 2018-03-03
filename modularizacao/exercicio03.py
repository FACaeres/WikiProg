def maior2(a, b):
   if a > b: return a
   else: return b

def maiorLista(a):
   maior = a<a href="0">0</a>
   for elem in a:
       if elem > maior:
           maior = elem
   return maior

dados = list(map(int,input().split()))
print(maiorLista(dados))
