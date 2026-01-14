# Ficha 7 Ex08

print(' Contador de Maiusculas')
#cadeia = input('Introduza a cadeia de catacteres: ')
cadeia = 'Subcadeias    Sao  Muito Lindas '

contador = 0
for l in cadeia:
    if l.isupper(): # o carater tem que ser uma LETRA maiuscula (para numeros e outros caracteres, retorna False)
        contador += 1
        print(f'{l}',end="")

print(f'\nA frase tem {contador} maiusculas')
#########################################

contador = 0
for i in cadeia:
    if i >='A' and i <= 'Z':
        contador += 1
        print(f'{i}',end="")

print(f'\nA frase tem {contador} maiusculas')
#########################################

#########################################

contador = 0
for i in cadeia:
    if i == i.upper() and(i.upper() != i.lower()):
        contador += 1
        print(f'{i}',end="")

print(f'\nA frase tem {contador} maiusculas')
#########################################


contador = 0
for i in cadeia:
    if i == i.upper()  and i.isalpha():
        contador += 1
        print(f'{i}',end="")

print(f'\nA frase tem {contador} maiusculas')
