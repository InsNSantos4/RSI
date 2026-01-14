# Ficha 10 Ex04


'''4. Implemente um programa para ler uma lista de 10 números inteiros positivos
 e imprimir quantas vezes aparece CADA algarismo.
O programa deve ser implementado com as seguintes funções:
Nome: lerLista
Descrição: Leitura de uma lista de 10 inteiros positivos
Parâmetros: Nenhum
Saída: Lista de 10 inteiros
Nome: contarNumeros
Descrição: Conta o número de ocorrências de cada algarismo numa lista
Parâmetros: Lista de 10 inteiros
Saída: Dicionário com o número de ocorrências de cada algarismo.'''

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



def contarNumeros(l_num):
    dic_num = dict() # inicializar dicionario para a contagem
    for i in range(len(l_num)): # percorrer a lista de numeros
        for algarismo in l_num[i]: # percorrer os algarismos de cada numero
            if algarismo in dic_num.keys(): # verifica se o algarismo ja existe no dicionario
                dic_num[algarismo] += 1 # se existe, adiciona mais um
            else:
                dic_num[algarismo] = 1 # não existe, cria a key col o value 1
    return dic_num

#programa principal
#invocar a função LerLista()  para obter a lista de input
lista_num = LerLista()

print('Lista: ',lista_num)




#invocar a função contarNumeros para obter o nº de ocorrências
dic_contagem  = contarNumeros(lista_num)
print('Dicionario da contagem:', dic_contagem)
print()

# Para imprimir por ordem:
keys_ordenadas = list(dic_contagem.keys()) # criar lista com a keys
keys_ordenadas.sort()  # ordenar a lista com as keys()
for key in keys_ordenadas:  # percorrer a lista com as keys() ordenadas
    print(key,dic_contagem[key]) # imprimir o par key , value

N = input('Qual o algarismo a contabilizar? :' )
print(f'Numero de ocorrências do algarismo {N}: {dic_contagem[N]} ')

