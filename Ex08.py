# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# A entrada do programa contém dois valores: um valor inteiro X representando a distância total percorrida (em Km),
# E um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.
# No final, apresente o valor que representa o consumo médio do automóvel seguido da mensagem "km/l";

d = int(input("\nDigite a distancia total percorrida pelo automóvel (em Km): "))
c = float(input("Digite o total de combustível gasto (em Litros): "))

consumo = d / c

print("\nO consumo médio do automóvel é de:", "{:.1f}".format(consumo), "km/l")