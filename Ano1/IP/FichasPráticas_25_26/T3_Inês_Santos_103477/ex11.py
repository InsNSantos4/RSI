# Ano bissexto
# 11. Escreva um programa que verifique se um determinado ano é ou não bissexto (um ano é
# bissexto se for divisível por 4 e não for divisível por 100, ou então também o será se for
# divisível por 400).

year = int(input("Ano: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("O ano inserido é bissexto.")
else:
    print("Não é ano bissexto.")