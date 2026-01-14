# IRS
# 9. Escreva um programa que permita calcular o valor do IRS a pagar por um trabalhador
# cujo salário anual é fornecido pelo utilizador.
# Assuma que o trabalhador deve pagar 10% de IRS se o seu salário anual for inferior a
# 10000 Euros. Caso contrário o imposto a ser pago é igual a 10% sobre 10000 Euros mais
# 25% sobre o restante valor.

salario_anual = float(input("Your yearly salary: "))

if salario_anual < 10000:
    irs = 0.1 * salario_anual
else:
    irs = (0.1 * 10000) + (0.25 * (salario_anual - 10000))
    
print("You should pay " + str(irs) + "€ of IRS this year.")