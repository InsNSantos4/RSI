#
# Ficha 8 Ex01
# IP Ficha 08  Exercicio 01
# pedrotomesa@ua.pt - RSI
# pop@ua.pt - CS

print('>>> Introduzir Matriz N x N e obter a matriz transporta' )

dim=int(input("\nIntroduza o tamanho (N) da matriz: "))

#print
for l in range(dim):
    for col in range(dim):
        print(f' C{l+1}.{col+1}',end=' ')
    print('')
print('')

#carregamento / introdução de dados

# inicialização da matriz
m= []
for l in range(dim): # percorre linha a linha
    m.append([]) # inicializa linha
    for col in range(dim): # percorre coluna a coluna
        val= int(input(f'C{l+1},{col+1}: ')) # lê o valor da celula
        m[l].append(val) # adiciona a celula


for l in range(dim):
    for col in range(dim):
        print(f' {m[l][col]} ', end=" ")
    print('')

# Calculo da Matriz transposta:
print('\n Matriz transposta:')
for col in range(dim):
    for l in range(dim):
        print(f' {m[l][col]} ', end=" ")
    print('')
