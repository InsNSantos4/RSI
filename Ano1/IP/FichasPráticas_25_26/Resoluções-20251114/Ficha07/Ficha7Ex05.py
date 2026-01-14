# Ficha 7 Ex05

print(' Sub cadeia de uma cadeia')
cadeia1 = input(' Introduza a 1ª cadeia de catacteres: ')
cadeia2 = input(' Introduza a 2ª cadeia de catacteres: ')



if cadeia2 in cadeia1 :
    print(f"{cadeia2} é subcadeia de {cadeia1}")
else:
    print(f'{cadeia2} NÃO é subcadeia de {cadeia1}')

#exit()


if len(cadeia1) > len(cadeia2):
    if cadeia2 in cadeia1 :
        print(f"{cadeia2} é subcadeia de {cadeia1}")
    else:
        print(f'{cadeia2} NÃO é subcadeia de {cadeia1}')
else:
    print('O comprimento da 1ª cadeia tem que ser maior que o da 2ª cadeia')