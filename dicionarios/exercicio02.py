vogais = {"a": 0, "e": 0, "i": 0, "o":0, "u":0}
frase = input()
for l in frase:
   if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
       vogais[l] += 1
print(vogais)
 
