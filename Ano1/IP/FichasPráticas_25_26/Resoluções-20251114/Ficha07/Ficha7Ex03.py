# Ficha 7 Ex03

print(' Subcadeias de comprimento 3 de uma cadeia')
cadeia = input('Introduza a cadeia de catacteres: ')

#cadeia = 'Subcadeias'# de comprimento'


for i in range(len(cadeia)-2):
    inicio = i
    final = i + 3
    print(cadeia[inicio:final],inicio,final)

print('\nOutra forma:\n')
for i in range(len(cadeia)):
    inicio = i
    final = i + 3
    if final >len(cadeia):
        break
    print(cadeia[inicio:final],inicio,final)
exit()

for i in range(len(cadeia)+2):
    inicio = i
    final = i + 3
    a=cadeia[inicio:final]
    print(cadeia[inicio:final],inicio,final)


for i in range(len(cadeia)+2):
    inicio = i
    final = i + 3
    a=cadeia[-final:-inicio]
    print(a,inicio,final)

for i in range(len(cadeia)+2):
    inicio = i
    final = i + 3
    a=cadeia[-7:5]
    print(a,inicio,final)
