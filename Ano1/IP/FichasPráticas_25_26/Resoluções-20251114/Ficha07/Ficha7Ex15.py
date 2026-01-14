# Ficha 7 Ex15

print("»»»»»»  Este programa elimina as vogais de um texto")
print("»»»»»»\n ")


texto = input('Introduza o texto: ')
novo_texto =""
for letra in texto:
    if letra.lower() in "aeiou":
        continue
    else:
        novo_texto += letra

print(f'\nNovo texto:')
print(novo_texto)
