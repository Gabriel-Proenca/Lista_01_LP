# Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de combustível,
# Em que são fornecidos a altura e o raio deste cilindro.
# Sabe-se que: A lata de tinta custa $ 50,00. Cada lata tem 5 litros.
# Cada litro de tinta pinta 3 metros quadrados.
# Dica: você vai precisar primeiro calcular a área do cilindro, para saber quantos metros quadrados vai precisar pintar,
# para depois calcular o custo e a quantidade de tintas.
# Para calcular a área do cilindro, utilize a fórmula: A = πr² + 2πrh (r = raio e h = altura do tanque).
# obs: Na verdade a formula é: A = (2 * πr²) + 2πrh

#Importar math para utilizar pi e a função de arredondamento
import math

#Irei utilizar funções para facilitar 

def calc_area(r,h):

    area_total = round((2*(math.pi * (r*r))) + (2 * math.pi * r * h))
    return area_total

def calc_latas(area, litros_metro):
    litros_total = area / litros_metro
    latas_total = math.ceil(litros_total / litros_lata)
    return latas_total

custo_lata = 50
litros_lata = 5
litros_metro = 3

r = float(input("\nDigite o raio do cilindro em metros: "))
h = float (input("Digite a Altura do cilindro em metros: "))

area = calc_area(r, h)
latas = calc_latas(area, litros_metro)
custo_total = latas * custo_lata

print("Quantidade de latas de tinta necessárias", latas)
print("Custo toal de latas: R$ ", custo_total)