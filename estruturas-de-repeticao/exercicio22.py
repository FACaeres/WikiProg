from math import *
n = int(input())
i = 1
while i <= n:
    # saida formatada para exibir apenas 
    # duas casas decimais
    print('{} {} {:.2f} {:.2f}'.format(i, i**2, log(i), sin(i)))
    i += 1
