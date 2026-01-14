# Ficha 10 Ex05

'''Escreva uma função que receba, por parâmetro, uma matriz A quadrada e a sua dimensão,
multiplicando a soma de todos os elementos de cada linha pelo elemento
da diagonal principal da própria linha.
Retorne a soma de todos os valores calculados
Implemente um programa que permita testar a função desenvolvida.'''


def f_mat(matriz,d):
    soma_total = 0 # soma total
    for linha in range(d): # percorrer as linhas
        soma_linha=0 # soma dentro a linha
        #soma da linha (percorre todas as colunas da linha):
        for coluna in range(d): # percorrer as colunas da linha
            soma_linha = soma_linha + matriz[linha][coluna] # somar os elemento da linha
        # outra forma:
        # soma_linha = sum(matriz[linha]) # somar os elemento da linha (lista matriz[linha] )
        # multiplica a soma da linha pela diagonal: diagonal é qd linha = coluna
        s_linha_diag = soma_linha * matriz[linha][linha]
        soma_total = soma_total + s_linha_diag
    return soma_total

mat = [ [1,2,3],[2,3,4],[3,4,5]]


print(f_mat(mat,3))

