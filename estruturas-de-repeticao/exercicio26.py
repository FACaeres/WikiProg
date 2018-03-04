a = int(input())
b = int(input())
for numero in range(a, b+1):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    if primo:
        print(numero)
