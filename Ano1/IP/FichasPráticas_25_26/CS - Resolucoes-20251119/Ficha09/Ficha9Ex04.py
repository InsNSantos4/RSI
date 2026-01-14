# Ficha9 Ex04

'''Crie um dicionário com o nome 'idades', vazio,
 que servirá para guardar nomes de pessoas e as
 respetivas idades. De seguida, peça ao utilizador
 nomes de pessoas e as respetivas idades.
 Vá acrescentando estas informações ao dicionário.
 Caso o nome introduzido já exista, deverá apresentar
  uma mensagem em conformidade'''

# inicialização do dic
nomes = {}

#leitura de dados:
while True:
    nome = input('Digite o nome do individuo (x para terminar): ')
    if nome.lower() == 'x':
        break
    elif nome in nomes: # nome já existe no dicionario
        print ('--> Nome já existente. Entrada inválida <--'  )
        continue #volta ao inicio do loop
    #leitura da idade
    idade = int(input('Digite a idade: '))
    # adiciona novo item ao dicionário:
    nomes[nome] = idade

# a) Apresente no ecrã o dicionário completo;
print('\n a) Dicionário: ')
print(nomes)

# b) Apresente no ecrã o tamanho do dicionário (n. de entradas);
print(f'\n b) Tamanho do Dicionário: {len(nomes)}')

# c) Apresente no ecrã a lista das pessoas que fazem parte do dicionário;
print('\n c) Lista das pessoas que fazem parte do dicionário:  ')
l_nomes= list(nomes.keys())
print(l_nomes)
for nome in nomes:
    print(f'  {nome}')

# d) Apresente no ecrã a lista das idades que fazem parte do dicionário;
idades1 = nomes.values()
idades = list(idades1)
print('\n d) Lista das idades que fazem parte do dicionário:  ')
print(f'  {idades}')


# e) Crie uma lista ordenada dos nomes das pessoas que fazem parte do dicionário e apresente-a no ecrã;
# nomes :
nomes1=list(nomes)
nomes1.sort()
print('\n e) Lista ordenada das pessoas que fazem parte do dicionário:  ')
print(f'  {nomes1}')
# outra forma:
nomes2= nomes.keys()
nomes3= list(nomes2)
nomes3.sort()
print(f'  {nomes3}')

#f) Apresente o dicionário no ecrã, ordenado por ordem alfabética de nomes;
# nomes1 : lista ordenada de nomes
print('\n f) Dicionário ordenado por ordem alfabética de nomes: ')
for nome in nomes1:
    print(f' Key - "{nome}"  value - {nomes[nome]}')

#g) Peça ao utilizador um nome, elimine a respetiva entrada no dicionário e apresente-o novamente, ordenado.
nome_apagar= input('\n g) Qual o nome que pretende apagar?: ')
#apagar no dicionário:
if nome_apagar in nomes.keys():
    del(nomes[nome_apagar])
else:
    print('Nome não faz parte da lista')
nomes1 = list(nomes.keys())
nomes1.sort()
print('\nDicionário ordenado por ordem alfabética de nomes: ')
for nome in nomes1:
    print(f' Key - "{nome}"  value - {nomes[nome]}')