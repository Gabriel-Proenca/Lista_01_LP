def calc_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    qtd_notas = [0] * len(notas)

    for i in range(len(notas)):
        qtd_notas[i] = valor // notas[i]
        valor %= notas[i]

    return qtd_notas

valor = int(input("\nDigite o valor de notas: "))

notas = calc_notas(valor)

print("\nNotas necessárias:")
for i in range(len(notas)):
    print(notas[i]," notas de r$", [100, 50, 20, 10, 5, 2, 1][i])
