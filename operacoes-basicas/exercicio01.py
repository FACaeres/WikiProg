# Resolucao

quantidade_cabecas = int(input("Digite a quantidade de cabecas: ")) 

quantidade_pes = int(input("Digite a quantidade de pes: ")) 

quantidade_lobos = (quantidade_pes-2*quantidade_cabecas)//2 

quantidade_cacadores = quantidade_cabecas - quantidade_lobos 

print("Ha ", quantidade_cacadores, "cacadores e ", quantidade_lobos, "lobos")

