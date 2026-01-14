# Ficha 7 Ex14

print("»»»»»»  Este programa verifica se uma palavra é alfabética")
print("»»»»»»\n ")


palavra = input('Introduza a palavra: ')
palavra = palavra.lower()
alfa = True
l_palavra = len(palavra)
for i in range(1,l_palavra):
    if palavra[i-1] > palavra[i]:
        alfa = False
        break


if alfa:
    print("A palavra é alfabética")
else:
    print("A palavra NÃO é alfabética")

# fim