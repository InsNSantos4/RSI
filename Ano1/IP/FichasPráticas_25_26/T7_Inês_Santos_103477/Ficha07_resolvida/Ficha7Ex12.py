# Ficha 7 Ex12

print("»»»»»»  Este programa verifica se os parentesis estão estruturados")
print("»»»»»»\n ")


texto = input('Introduza o texto: ')

contador_abre = 0
contador_fecha = 0

for carater in texto:
    if carater == "(":
        contador_abre += 1
    elif carater == ")":
        contador_fecha += 1

    if contador_fecha > contador_abre:
        # parentesis fechou antes de abrir
        break

if contador_abre  ==  contador_fecha :
    print("O texto tem os parêntesis BEM estruturados")
else:
    print("O texto tem os parêntesis MAL estruturados")

# fim