# Escreva um programa que leia as coordenadas x e y de pontos no R2 e
# calcule sua distância da origem (0,0). Dica: use a formula D = RAIZ(x^2 + y^2)

#Para usar a função RAIZ é necessário importar a função "math"
import math

x = float(input("\nDigite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

d = round(math.sqrt((x*x) + (y*y)), 2)
print ("\nA diatância de origem é: ", d)
