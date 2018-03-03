from math import sqrt

def distancia(pontoA, pontoB):
   parcialX = (pontoA["X"] - pontoB["X"])**2
   parcialY = (pontoA["Y"] - pontoB["Y"])**2
   return sqrt(parcialX+parcialY)

A = {"X": 0, "Y": 0}
B = {"X": 0, "Y": 0}

A["X"] = int(input("X de P1: "))
A["Y"] = int(input("Y de P1: "))
print()
B["X"] = int(input("X de P2: "))
B["Y"] = int(input("Y de P2: "))

print(distancia(A,B))
