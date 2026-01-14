# Ficha 7 Ex04

print(' Prefixo de uma cadeia')
cadeia1 = input(' Introduza a 1ª cadeia de catacteres: ')
cadeia2 = input(' Introduza a 2ª cadeia de catacteres: ')
#cadeia = 'Subcadeias'# de comprimento'

l2= len(cadeia2)
if cadeia2 == cadeia1[:l2] :
    print(f"{cadeia2} é prefixo da {cadeia1}")
else:
    print(f'{cadeia2} NÃO é prefixo da {cadeia1}')

