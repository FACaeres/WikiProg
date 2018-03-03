"""Resolução""".

# Pede ao usuário a quantidade de números 

n = int(input()) 

# Inicializa a soma 

soma = 0

# Pede os números ao usuário e os soma 

for i in range(n): 

   numero = int(input()) 

   soma += numero

# Calcula a media dos numeros 

media = soma/n

# Exibe o resultado 

print(media)
