# Receba o salário-base de um funcionário.
# Calcule e imprima o salário a receber,
# sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
# Além disso, ele paga 7% de imposto sobre o salário-base

s_base = float(input("\nInforme o salário-base de um funcionário: R$ "))
g = float(s_base * 0.05)
i = float(s_base * 0.07)
s_receber = round(s_base + g - i, 2)
print("\nO salário a receber será de: R$", s_receber)