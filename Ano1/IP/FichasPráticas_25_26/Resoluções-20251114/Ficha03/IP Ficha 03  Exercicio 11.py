#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 11
#
# Ano bissexto
# 11. Escreva um programa que verifique se um determinado ano é ou não bissexto (um ano é
# bissexto se for divisível por 4 e não for divisível por 100, ou então também o será se for
# divisível por 400).

print("\n»»»»»» ")
print("»»»»»»  Este programa verifica se um determinado ano é ou não bissexto ")
print("»»»»»»\n ")

# Ler o Ano
ano = int(input("Qual o ano que pretende verificar se é bissexto?: "))


if (ano%4 ==0 and  ano%100 !=0) or (ano%400 ==0):
     print("O ano", ano, "é ano bissexto")
else:
    print("O ano", ano, "é um ano comum")



# fim do programa

