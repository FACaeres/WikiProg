totExerc = int(input())
qtdExerc = int(input())
qtdDin = float(input())
porc = (qtdExerc/totExer)*100
if(porc >= 80):
	if(qtdDin >= 200):
		print(“Maria vai viajar”)
	else:
		print(“Maria nao vai viajar”)
else:
	print(“Maria nao vai viajar”)
