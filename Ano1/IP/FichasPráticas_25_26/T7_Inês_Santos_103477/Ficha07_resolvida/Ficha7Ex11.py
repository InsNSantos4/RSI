# Ficha 7 Ex11

print("»»»»»»  Este programa apresenta os numeros contidos numa cadeia de caracteres")

cadeia = input('Introduza a cadeia de caracteres: ')
contador = 0

palavras = cadeia.split(" ")
for pal in palavras:
    if pal.isdigit():
        contador +=1
        print(pal)

print(f'Quantidade de numeros na cadeia: {contador}')
