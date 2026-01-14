# Implemente um programa para ler uma lista de 10 números inteiros positivos e imprimir
# quantas vezes aparece o algarismo N, sendo N fornecido pelo utilizador do programa.
# O programa deve ser implementado com as seguintes funções:
#
# Nome: lerLista
# Descrição: Leitura de uma lista de 10 inteiros positivos
# Parâmetros: Nenhum
# Saída: Lista de 10 inteiros
#
# Nome: contarNumeros
# Descrição: Conta o número de ocorrências de um dado algarismo numa lista
# Parâmetros: Lista de 10 inteiros; número inteiro representando o algarismo a procurar
# Saída: Inteiro representando o número de ocorrências do algarismo procurado.


# Função de leitura de uma lista de 10 inteiros positivos
def lerLista():
    #ler uma lista de 10 inteiros:
    ten_integers_list = []
    for i in range(10):
        num = int(input(f"Introduza o {i+1}º número inteiro positivo da lista: "))
        while num < 0:
            num = int(input(f"Introduza o {i+1}º número inteiro positivo da lista: "))
        else:
            ten_integers_list.append(num)
    print("\n")
    return ten_integers_list

# Função que conta o nº de ocorrências de um dado algarismo numa lista
def contarNumeros(ten_ints_list, element_to_count):
    num_ocurrences = 0
    for i in range(len(ten_ints_list)):
        if ten_ints_list[i] == element_to_count:
            num_ocurrences += 1
    return num_ocurrences


# programa:
# ler uma lista de 10 nºs inteiros positivos
lista_dez_elems = lerLista()

# imprimir quantas vezes aparece o algarismo N (fornecido pelo utilizador)
n = int(input("Introduza o algarismo N que quer procurar e contar na lista: "))
print()
print(f"O algarismo {n}, que introduziu, aparece {contarNumeros(lista_dez_elems, n)} vezes na lista.")