valor = float(input())
p = float(input())
meses = int(input())

total = valor

for i in range(meses):
    total += total * p

print(total)
