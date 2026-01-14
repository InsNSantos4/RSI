#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 09
#
# IRS
# 9. Escreva um programa que permita calcular o valor do IRS a pagar por um trabalhador
# cujo salário anual é fornecido pelo utilizador.
# Assuma que o trabalhador deve pagar 10% de IRS se o seu salário anual for inferior a
# 10000 Euros. Caso contrário o imposto a ser pago é igual a 10% sobre 10000 Euros mais
# 25% sobre o restante valor


print("\n»»»»»» ")
print("»»»»»»  Este programa calcula o valor do IRS a pagar en função do salário anual")
print("»»»»»»\n ")

# Ler o valor do salário anual
salario_A = float(input("Qual o valor o valor do seu salário anual? :  € "))

if salario_A < 10000:
    irs = salario_A * 0.1  # IRS 10%  (10/100 = 0.1)
else:
    irs_10 = 10000 * 0.1  # IRS 10%
    irs_25 = (salario_A - 10000) * 0.25  # IRS 25%  (remanescente após os €10 000)
    irs = irs_10 + irs_25  # Total IRS
    #    irs = 1000 + (Salario_A - 10000) * 0.25

print("Valor do IRS a pagar é de  €", irs)

# fim do programa

irs= salario_A*0.1 * (salario_A <= 10000) + (1000 + (salario_A-10000)*0.25) * (salario_A > 10000)
print("Valor do IRS a pagar é de  €", irs)