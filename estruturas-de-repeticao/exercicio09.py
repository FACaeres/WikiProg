numeroAdivinhacao = 14

chute = int( input("Jogador, tente adivinhar o numero: "))

while chute != numeroAdivinhacao:

   if chute < numeroAdivinhacao:

       print ("Errou!, O numero e maior")

   elif chute > numeroAdivinhacao:

       print ("Errou!, O numero e menor")

   chute = int( input("Jogador, tente adivinhar o numero: "))

print( "Parabens!!! Voce acertou o numero!") 
