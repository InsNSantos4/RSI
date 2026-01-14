# Ficha 7 Ex09a

print("»»»»»»  Este programa calcula numa cadeia de caracteres quantas "
      "palavras de dimensão k se encontram na cadeia de caracteres")
print("»»»»»»\n ")


cadeia = input('Introduza a cadeia de catacteres: ')
k= int(input('Introduza o valor de K: '))

#retirar brancos no inicio e final da cadeia
cadeia = cadeia.strip()
cadeia +=" "

#retirar espaços com mais que 1 branco
while cadeia.find('  ') > 0:
    cadeia=cadeia.replace('  ',' ')
print (cadeia)


# percorrer a cadeia
contador = 0
palavra =""
cadeia +=" " # colocar um branco no final para identificar o fim da frase
for letra in cadeia:
    if letra != " ":
        palavra += letra
    else:
        if len(palavra) == k:
            contador += 1
        palavra = ""
print (cadeia)

print(f'Numero de palavras de comprimento {k} na cadeia: {contador}')

