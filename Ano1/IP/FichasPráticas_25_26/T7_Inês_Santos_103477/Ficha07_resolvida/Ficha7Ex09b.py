# Ficha 7 Ex09b

print("»»»»»»  Este programa calcula numa cadeia de caracteres quantas "
      "palavras de dimensão k se encontram na cadeia de caracteres")
print("»»»»»»\n ")


cadeia = input('Introduza a cadeia de catacteres: ')
k= int(input('Introduza o valor de K: '))

#retirar brancos no inicio e final da cadeia
cadeia = cadeia.strip()

# percorrer a cadeia
contador = 0
palavra =""
cadeia +=" " # colocar um branco no final para identificar o fim da frase
for i in range(len(cadeia)):
    if cadeia[i] != " ":
        palavra += cadeia[i]
    else:
        if len(palavra) == k:
            contador += 1
        palavra = ""


print(f'Numero de palavras de comprimento {k} na cadeia: {contador}')