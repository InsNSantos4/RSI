#
# POP Setembro 2023
#
# IP Ficha 02  Exercicio 03
#
# Escreva um programa que armazene dois números em variáveis e troque os valores das variáveis.

# Ler Variável 1
# Ler Variável 2
# Criar Variavel 3  e guardar nela o valor de Variavel 1  (V3 = V1)
# Colocar na Variavel 1 o valor de Variavel 2 (Agora V1 = V2 )
# Colocar na Variavel 2 o valor de Variavel 3 (Agora V2 = V3 (valor inicial de V1 )
# Printar os valores das variaveis 1 e 2

# Entrada de dados
V1=int(input("Entre o valor da variavel 1: "))    # Ler Variável 2
V2=int(input("Entre o valor da variavel 2: "))    # Ler Variável 1

# Resolução do pedido
V3 = V1      # Criar Variavel 3  e guardar nela o valor de Variavel 1  (V3 = V1)
V1 = V2      # Colocar na Variavel 1 o valor de Variavel 2 (Agora V1 = V2 )
V2 = V3      # Colocar na Variavel 2 o valor de Variavel 3 (Agora V2 = V3 que tem o valor inicial de V1 )

# Saida dos resultados
print('Novo valor da variavel 1: ',V1)
print('Novo valor da variavel 2: ',V2)


# Printar os valores das variaveis 1 e 2