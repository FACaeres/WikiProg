lista = [0] * 5
for i in range(5):
   lista[i] = {"nome": "", "esporte": "", "idade": 0, "altura": 0.0}

mais_alto = 0 #indice na lista do mais alto
mais_velho = 0 #indice na lista do mais velho
for cont in range(5):
   print("Informacoes do atleta", cont+1)
   lista[cont]["nome"] = input("Nome: ")
   lista[cont]["esporte"] = input("Esporte: ")
   lista[cont]["idade"] = int(input("Idade: "))
   lista[cont]["altura"] = float(input("Altura: "))

if lista[cont]["idade"] > lista[mais_velho]["idade"]:
       mais_velho = cont
   if lista[cont]["altura"] > lista[mais_alto]["altura"]:
       mais_alto = cont
   print()

print("Mais alto:", lista[mais_alto]["nome"], "com", lista[mais_alto]["altura"])
print("Mais velho:",lista[mais_velho]["nome"], "com", lista[mais_velho]["idade"])
