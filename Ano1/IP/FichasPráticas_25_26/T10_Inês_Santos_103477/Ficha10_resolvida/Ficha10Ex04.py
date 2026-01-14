# Ficha 10 Ex04


'''4. Implemente um programa para ler uma lista de 10 números inteiros positivos e imprimir quantas vezes aparece o algarismo N, sendo N fornecido pelo utilizador do programa.
O programa deve ser implementado com as seguintes funções:
Nome: lerLista
Descrição: Leitura de uma lista de 10 inteiros positivos
Parâmetros: Nenhum
Saída: Lista de 10 inteiros
Nome: contarNumeros
Descrição: Conta o número de ocorrências de um dado algarismo numa lista
Parâmetros: Lista de 10 inteiros; número inteiro representando o algarismo a procurar
Saída: Inteiro representando o número de ocorrências do algarismo procurado.'''

def LerLista():
    print('Introduza 10 numeros inteiros positivos: ')
    contador = 1 # contador de contarNumeros
    lista = []   #  nicializar a lista
    while contador <= 10:
        n = input(f' Digite o {contador}º numero: ')
        if n.isdigit():
            lista.append(n)
            contador += 1
        else:
            print('>>> Valor Inválido <<<')
            continue
    return lista



def contarNumeros(l_num,n):
    contador = 0  # Inicializar contador do digito:
    for i in range(10):
        contador += l_num[i].count(n)
    return contador

#programa principal
#invocar a função LerLista()  para obter a lista de input
lista= LerLista()
print(lista)

N = input('Qual o algarismo a contabilizar? :' )

#invocar a função contarNumeros para obter o nº de ocorrências
N_total = contarNumeros(lista,N)

print(f'Numero de ocorrências do algarismo {N}: {N_total} ')

################################################################
####  Para dar a contagem de todos os algarismos:
print('\nContagem de todos os algarismos:')
for algarismo in range(10): # percorrer os algarismos
    print(f'{algarismo} - {contarNumeros(lista,str(algarismo))} ') # invocar contarNumeros para cada algarismo

