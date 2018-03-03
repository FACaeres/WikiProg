base = -1 

expoente = -1

while base < 0 or expoente < 0:       

   base,expoente = map(int,input("Base e expoente: ").split())       

   if base < 0 or expoente < 0:             

       print("Dados inválidos!")             

       print("Digite uma nova base e expoente.")

resultado = 1 

for contador_it in range(expoente):       

   resultado *= base 

print(base,"^",expoente,"=",resultado)

