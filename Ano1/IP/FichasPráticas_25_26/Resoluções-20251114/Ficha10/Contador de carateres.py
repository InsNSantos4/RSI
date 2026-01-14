'''
Contador de caracteres.
Criar função que receba uma string e devolva o nº de ocorências de cada caractere
Nome: contaCar
Descrição:  Recebe uma string e devolva o nº de ocorrências de cada caractere
Parâmetros: uma string
Saída: Dicionário com key-> caratere  value-> nº de ocorrências
'''

def contaCar(string):
    dic_car = dict() # inicializar dicionario para a contagem
    for car in string: # percorrer a string
            if car in dic_car.keys(): # verifica se o algarismo ja existe no dicionario
                dic_car[car] += 1 # se existe, adiciona mais um
            else:
                dic_car[car] = 1 # não existe, cria a key col o value 1
    return dic_car

#programa principal
frase = input('Contador de caracteres.\nDigite uma frase: ')

#invocar a função contaCar para obter o nº de ocorrências
dic_contagem  = contaCar(frase)
print('Dicionario da contagem:', dic_contagem)
print()

# Para imprimir por ordem:
keys_ordenadas = list(dic_contagem.keys()) # criar lista com a keys
keys_ordenadas.sort()  # ordenar a lista com as keys()
for key in keys_ordenadas:  # percorrer a lista com as keys() ordenadas
    print(key,dic_contagem[key]) # imprimir o par key , value


