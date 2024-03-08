def calc_notas(valor):
    notas_100 = valor //100             # calcula primeiro as notas de 100
    valor %= 100                        # para de acordo com o resultado atribuir
    notas_50 = 0                        #valor as outras notas
    notas_20 = 0
    notas_10 = 0
    notas_05 = 0
    notas_02 = 0
    notas_01 = 0

    if valor>=50:
        notas_50 = valor // 50
        valor %= 50
    
    if valor>=20:
        notas_20 = valor // 20
        valor %= 20

    if valor>=10:
        notas_10 = valor // 10
        valor %=10
    
    if valor>=5:
        notas_05 = valor // 5
        valor %= 5
    
    if valor>=2:
        notas_02 = valor // 2
        valor %= 2
    
    notas_01 = valor

    return notas_100, notas_50, notas_20, notas_10, notas_05, notas_02, notas_01

valor = int(input("\nDigite o valor de notas: "))

notas_100, notas_50, notas_20, notas_10, notas_05, notas_02, notas_01 = calc_notas(valor)

print("\nNotas necessárias:")
print(notas_100,"Notas de 100")
print(notas_50,"Notas de 50")
print(notas_20,"Notas de 20")
print(notas_10,"Notas de 10")
print(notas_05,"Notas de 5")
print(notas_02,"Notas de 2")
print(notas_01,"Notas de 1\n")
