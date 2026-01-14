# Ficha 7 Ex10a

print("»»»»»»  Este programa apresenta os numeros contidos numa cadeia de caracteres")

cadeia = input('Introduza a cadeia de caracteres: ')

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
        if palavra.isdigit():  #
            contador += 1
            print(palavra)
        palavra = ""


print(f'Quantidade de numeros cadeia: {contador}')