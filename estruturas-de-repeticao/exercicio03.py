palavra = ""

contador_maiores5 = 0

while palavra != "fim":

   palavra = input("Digite uma palavra: ")

   if len(palavra) > 5 and palavra != "fim":

       contador_maiores5 = contador_maiores5 + 1

print("Palavras com mais de 5 caracteres",contador_maiores5)
