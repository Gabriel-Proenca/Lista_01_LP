# Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de combustível,
# Em que são fornecidos a altura e o raio deste cilindro.
# Sabe-se que:  A lata de tinta custa $ 50,00.  Cada lata tem 5 litros.
# Cada litro de tinta pinta 3 metros quadrados.
# Dica: você vai precisar primeiro calcular a área do cilindro, para sabe quantos metros quadrados vai precisar pintar,
# para depois calcular o custo e a quantidade de tintas.
# Para calcular a área do cilindro, utilize a fórmula: A = πr² + 2πrh (r = raio e h = altura do tanque).

#Importar math para utilizar pi e a função de arredondamento
import math

#Irei utilizar funções para facilitar 

def calc_area(r,h)
    area_b = math.pi * r * h
    area_l = 2 * math.pi * raio * altura
    area_total = 2 * area_b + area_l
    