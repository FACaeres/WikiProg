n = int(input())
soma = 1
for i in range(1,n+1)
    fat = 1
    for cont in range(1, i+1):
        fat = fat*cont
        soma = soma + 1/fat
print(soma)
