# Ficha 8 Ex 04

# Escreva um programa capaz de ler uma matriz M5x5 e calcular o maior elemento
# de cada linha da matriz e a média dos elementos de cada coluna.
#
n=int(input('Dimensão da matriz (nxn):'))
# Ler matriz:
m =[]
for l in range(n):
    m.append([])
    for col in range(n):
        val= int(input(f'Introduza o valor de C{l+1}.{col+1}:'))
        m[l].append(val)
print(m)
print('')

# Valor máximo  da linha:
for l in range(n):
    maximo = max(m[l])
    print(f' Max Linha {l+1}: {maximo} ')

print('')
# Média de cada coluna:
for col in range(n):
    soma = 0
    for l in range (n):
        soma += m[l][col]
    print(f' Média coluna {col+1}: {soma/n}')
