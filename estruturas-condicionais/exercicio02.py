categoria = int(input("Digite a categoria do produto: ")) 

if categoria == 1: 

     preco = 10 

else: 

     if categoria == 2: 

         preco = 18 

     else:

          if categoria == 3: 

             preco = 23 

         else: 

             if categoria == 4: 

                 preco = 26 

             else: 

                 print("Categoria invalida!") 

                 preco = 0 

print("O preco do produto e: R$%.2f" %preco) 

