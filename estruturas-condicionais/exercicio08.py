""" Pedindo tres numeros inteiros para o usuario"""

a = int( input () )

b = int( input () )

c = int( input () )

"""O numero eh maior se for maior que os outros dois"""

if a > b and a > c:

  print (a)

elif b > a and b > c:

  print (b)

elif c > a and c > b:

  print (c)

else:

  print ("numeros iguais") 
