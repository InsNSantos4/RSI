# Ficha 8 Ex 08

#Desenvolva um programa que permita ao utilizador introduzir texto até introduzir o
#carácter #, devolvendo como output as seguintes estatísticas de texto:
#   a) Número total de caracteres;
#   b) Número total de palavras
#   c) Número total de linhas;
#   d) Contagem de ocorrências por letra do abecedário
# Considere que o utilizador introduz somente caracteres em minúsculas. Assim, deverá
# gerar as estatísticas de ocorrência para cada uma das letras do abecedário (a,b,c, …, y, z).

# vamos criar uma lista texto[] para conter o texto
# e uma "sub-lista" para cada linha (cada elemento da lista texto é uma linha:

texto=[]

#leitura
while True:
    linha = input('Digite o texto: ')
    if '#' in linha: #saida pelo catactere '#'
        break
    texto.append(linha) # cada elemento fica com uma linha
print(texto)

# nº de linhas:
# Como elemento de texto[:], o numero de linhas é o nº de elementos de texto
num_linhas = len(texto)
print(' Numero de linhas:', num_linhas)

# nº de caracteres:
# percorer a lista texto, contando o tamanho de cada elemento (linha)
num_carateres = 0
for i in range(len(texto)):
    num_carateres += len(texto[i])
print(' Numero de caracteres:', num_carateres)

# nº de palavras:
num_palavras = 0
for i in range(len(texto)):
    list_pal = texto[i].split()
    n_pal = len(list_pal)
    num_palavras += n_pal
print(' Numero de palavras:', num_palavras)

#contagem de letras
letras = 'abcdefghijklmnopqrstuvwxyz'
print(' Numero de letras:')
for l in letras:
    conta_letras = 0
    for i in range(len(texto)):
        linha = texto[i].lower()
        conta_letras += linha.count(l)
    if conta_letras > 0:
        print(f' {l}: {conta_letras}')