from random import randint
n = randint(1, 1000)
acertou = False
while not acertou:
    x = int( input() )
    if x == n:
        print('Acertou')
        acertou = True
    elif x < n:
        print('Tente um número maior')
    else:
        print('Tente um número menor')
