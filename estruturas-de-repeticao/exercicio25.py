texto = input()
c = input()
numvezes = 0
for p in range(len(texto)):
    if texto[p] == c:
        numvezes += 1
print(numvezes)
