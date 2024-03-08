# Criar um algoritmo que receba como entrada os valores dos catetos de um triângulo retângulo
# e com base no Teorema de Pitágoras (HIPOTENUSA² = CATETO1² + CATETO2²)
# O algoritmo deve imprimir o valor da hipotenusa, que é igual a raiz quadrada da soma dos quadrados dos catetos. 
# Dica: para este cálculo, é necessário calcular a raiz quadrada de um número. Considere o comando RAIZ(x); que calcula a raiz quadrada de x.

import math

c1 = float(input("\nDigite o valor do primeiro cateto: "))
c2 = float(input("Digite o valor do segundo cateto: "))

h = round (math.sqrt((c1 * c1) + (c2 * c2)),2)

print("\nO valor da hipotenusa deste triângulo é: ", h)