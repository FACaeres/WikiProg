"""Resolução""".

def pedir_codigo(minimo, maximo): 

   while True: 

       codigo = int(input("Digite o código: ")) 

       if minimo <= codigo <= maximo: 

           return codigo 

       else:

           print("Código inválido!")

def principal(): 

   print(pedir_codigo(10, 20))

principal()
