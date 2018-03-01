#recebe as notas
n1 = float(input("Digite n1:"))
n2 = float(input("Digite n2:"))
n3 = float(input("Digite n3:"))
p1 = float(input("Digite p1:"))
p2 = float(input("Digite p2:"))
p3 = float(input("Digite p3:"))

#calcula a nota final
NF = (p1*n1 + p2*n2 + p3*n3)/(p1+p2+p3)

#testa se foi aprovado
if NF >= 60:
	print("Aprovado", NF)
else:
	print("Reprovado", NF)
