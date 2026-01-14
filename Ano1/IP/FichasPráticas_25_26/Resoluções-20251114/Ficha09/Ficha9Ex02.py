#Ficha9 Ex02

# Lista para armazenar os frutos:
frutos = ['Ananas','Laranja','Banana','Castanha','Kiwi','Pera','Figo','Ameixa','Maçã']

# Lista para armazenar quantidades:
quantidade  = [10,55,32,250,70,35,28,35,90]

# forma 1
print('############### Forma  1: ')
# inicialização do dicionário:
dicionario1 = dict()
for i in range (len(frutos)):
    dicionario1[frutos[i]] = quantidade[i]

print(f"Dicionario: {dicionario1 }")

# forma 2:
print('\n############### Forma  2: ')
# Construção do dicionário
d = zip(frutos,quantidade)
# conversão em dicionario
dicionario = dict(d)
print(f"Dicionario: {dicionario }")



print('\n############### : ')
print("\n### dicionario:")
for key in dicionario:
    print("Chave:",key,"- valor:",dicionario[key])

# output
print("\n### items:")
for f,q in dicionario.items():
    print(f,q)
print()
print("\n### Lista items:")
lista = list(dicionario.items())
print(lista)

print("\n### tuplos:")
for z in lista:
    print(z)


print("\n### items:")
for f,q in lista:
    print(f,q)



