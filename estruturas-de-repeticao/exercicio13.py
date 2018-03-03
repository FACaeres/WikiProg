"""Pedindo a quantidade de numeros do conjunto"""

n = int( input())

"""Inicializa variaveis que guardam a maior quantidade de divisores encontrada e o numero que tem essa maior quantidade"""

maior_nro_divisores = -1

nro_resultado = -1

"""Para cada numero do conjunto"""

for i in range (n):

   """Recebe o numero do usuario"""

   numero = int( input())

   """O trecho abaixo conta o numero de divisores desse numero"""

   nro_divisores = 0

   for j in range (1, numero):

       if numero % j = 0

           nro_divisores += 1

   """O trecho abaixo verifica se o numero eh o que tem a maior quantidade de divisores e o guarda"""

   if nro_divisores > maior_nro_divisores:

       maior_nro_divisores = nro_divisores

       nro_resultado = numero

"""Exbibindo resultado"""

print (nro_resultado, nro_divisores)
