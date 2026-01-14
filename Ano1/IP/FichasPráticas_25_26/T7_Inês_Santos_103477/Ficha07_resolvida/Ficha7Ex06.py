# Ficha 7 Ex06

print(' Eliminação de espaços em branco')
#cadeia = input('Introduza a cadeia de catacteres: ')
cadeia = 'Subcadeias    sao  muito lindas  '

nova_cadeia =""
branco1 = False
for i in range(len(cadeia)):
    if cadeia[i] == " ":
        if branco1 == True:
            continue
        else:
            nova_cadeia += cadeia[i]
            branco1 = True
    else:
        nova_cadeia += cadeia[i]
        branco1 = False
nova_cadeia = nova_cadeia.strip()
print(f'  Frase inicial: "{cadeia}"')
print(f'  Frase final  : "{nova_cadeia}"')


#exit()

print()
print("Usando o metodo str.replace()")
frase = cadeia.strip()  # elimina brancos dos extremos
while frase.find("  ") >= 0:
    frase = frase.replace("  ", ' ')


print(f'  Frase inicial: "{cadeia}"')
print(f'  Frase final  : "{frase}"')

# fim do programa