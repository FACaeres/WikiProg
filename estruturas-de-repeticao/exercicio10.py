nota = int( input( "Digite uma nota: "))

maiorNota = nota

menorNota = nota

while nota >= 0:

   if nota > maiorNota:

       maiorNota = nota

   if nota < menorNota:

       menorNota = nota

   nota = int( input( "Digite uma nota: "))

print( "Maior nota:", maiorNota, " ,menor nota", menorNota)
