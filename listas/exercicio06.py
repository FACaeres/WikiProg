# Programa: Fibonacci com Vetor (lista)
# Dados: n, i são inteiros, e fibo é vetor de inteiros
# Série usada: F0 = 1, F1 = 2, Fn = Fn-1 + Fn-2
n = int(input("Digite tamanho da série de fibonacci (maior que dois): "))
fibo = n*[0]
fibo[0] = 1
fibo[1] = 2
# Gerando a série de fibonacci:
i = 2
while i < n:
   fibo[i] = fibo[i-1] + fibo[i-2]
   i = i + 1
# Mostrando a série de fibonacci numa mesma linha:
i = 0
while i < n:
   print(fibo[i], end=" ")
   i = i + 1
print("\nObserve que cada membro da série é a soma dos dois anteriores")
