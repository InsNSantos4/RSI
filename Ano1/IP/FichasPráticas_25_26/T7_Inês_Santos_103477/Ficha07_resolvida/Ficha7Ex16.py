# Ficha 7 Ex16

print("»»»»»»  Este programa criptogrifa um texto")
print("»»»»»»\n ")


texto = input('Introduza o texto: ')
deslocamento = int(input('Introduza o deslocamento: '))

letras="abcdefghijklmnopqrstuvwxyz"
LETRAS=letras.upper()
num="0123456789"
cripto=""

for carater in texto:
    if carater in letras:
        l=letras.find(carater)
        d = (l + deslocamento)%26
        n_car= letras[d]
        cripto +=n_car
    elif carater in LETRAS:
        l=LETRAS.find(carater)
        d = (l + deslocamento)%26
        n_car= LETRAS[d]
        cripto +=n_car
    elif carater in num:
        ln=num.find(carater)
        dn = (ln + deslocamento)%10
        n_car= num[dn]
        cripto +=n_car
    else:
        cripto +=carater

print(cripto)