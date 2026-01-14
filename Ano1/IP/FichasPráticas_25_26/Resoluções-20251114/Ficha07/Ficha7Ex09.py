# Ficha 7 Ex09

print("»»»»»»  Este programa calcula numa cadeia de caracteres quantas "
      "palavras de dimensão k se encontram na cadeia de caracteres")
print("»»»»»»\n ")


cadeia = input('Introduza a cadeia de catacteres: ')
k= int(input('Introduza o valor de K: '))
contador = 0

palavras = cadeia.split()
for i in palavras:
    if len(i) == k:
        contador += 1

print(f'Numero de palavras de comprimento {k} na cadeia: {contador}')


#########################################