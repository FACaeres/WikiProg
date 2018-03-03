"""Resolução""".

from math import pi

def area_circulo(raio): 

   return pi*(raio**2)

def principal(): 

   raio = float(input()) 

   while (raio != 0): 

       print(area_circulo(raio)) 

       raio = float(input())

principal()

