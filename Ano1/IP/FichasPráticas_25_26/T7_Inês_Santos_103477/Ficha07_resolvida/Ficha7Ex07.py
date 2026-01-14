# Ficha 7 Ex07

print(' Inversão da cadeia')
#cadeia = input('Introduza a cadeia de catacteres: ')
cadeia = 'Subcadeias    sao  muito lindas '

#forma 1
inverso =""
for i in cadeia:
    inverso = i + inverso

print(f'  Frase invertida: "{inverso}"')
#######################################################

#forma 2
inverso = cadeia[::-1]

print(f'  Frase invertida: "{inverso}"')

#######################################################
#forma 3
inverso =""
for i in range(1,len(cadeia)+1):
    inverso = inverso + cadeia[-i]

print(f'  Frase invertida: "{inverso}"')
########################################################

#forma 4
inverso =""
for i in range(len(cadeia)):
    inverso = cadeia[i] + inverso

print(f'  Frase invertida: "{inverso}"')

#fim

