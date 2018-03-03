"""Resolução""".

def delta(a, b, c): 

   return b**2 - 4*a*c

def equacao2grau(a, b, c): 

   d = delta(a, b, c) 

   if d < 0: 

       return False, 0, 0 

   else: 

       x1 = (-b + d**0.5)/(2*a) 

       x2 = (-b - d**0.5)/(2*a) 

       return True, x1, x2

def principal(): 

   a, b, c = map(int, input("Digite os coeficientes: ").split()) 

   tem_raizes, raiz1, raiz2 = equacao2grau(a, b, c) 

   if tem_raizes: 

       print("As raizes sao:", raiz1, " e ", raiz2) 

   else: 

       print("Nao existem raizes!")

principal()

