# Ficha 7 Ex10

print("»»»»»»  Este programa conta os algarismos contidos numa cadeia de caracteres")

cadeia = input('Introduza a cadeia de caracteres: ')

# Forma 1:
print('Forma 1')
contador = 0

for car in cadeia:
    if car in "1234567890":
        contador += 1

print(f'Quantidade de algarismos na cadeia: {contador}')

############################################################

print('Forma 2')
contador = 0

for car in cadeia:
    if car.isdigit():  #
        contador += 1


print(f'Quantidade de algarismos na cadeia: {contador}')
###################################################################3

print('Forma 3')
contador = 0

for i in range(len(cadeia)):
    if cadeia[i].isdigit():  #
        contador += 1

print(f'Quantidade de algarismos na cadeia: {contador}')