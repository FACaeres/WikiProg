from math import sqrt

def delta(A,B,C):
   return B**2 - 4 * A * C

def encontrarRaizes(coef):
   D = delta(coef[0],coef[1],coef[2])
   raizes = [0]*2
   if D >= 0:
       raizes[0] = (-1*coef[1] - sqrt(D))/(2*coef[0])
       raizes[1] = (-1*coef[1] + sqrt(D))/(2*coef[0])
   return raizes

dados = list(map(int,input("A, B, C: ").split()))
resposta = encontrarRaizes(dados)
print("X1 = %.1f" %resposta[0])
print("X2 = %.1f" %resposta[1])
