# Ficha 10 Ex06


'''Para evitar erros de digitação em números de grande importância,
como o NIB (número de identificação bancária)
geralmente adiciona-se ao número um algarismo “verificador”.
Por exemplo o número 1841 é utilizado normalmente como 18414,
onde o 4 é o algarismo verificador. Ele é calculado da seguinte forma:
• Cada algarismo do número é multiplicado por um peso começando em 2 da direita
 para a esquerda. Para cada algarismo seguinte o peso é acrescido de 1.
 Somam-se os produtos obtidos.
1*5 + 8*4 + 4*3 + 1*2 = 51
Calcula-se o resto da divisão desta soma por 11:
51 % 11 = 7
• Subtrai-se de 11 o resto obtido:
11 – 7 = 4
• Se o valor obtido for 10 ou 11, o dígito verificador será o 0. Nos restantes casos o algarismo verificador é o próprio valor encontrado
Escreva um programa que leia um número indeterminado de valores inteiros entre 1 a 999, e que para cada número imprima o seu correspondente algarismo verificador. O programa termina ao ser fornecido um número fora da faixa estabelecida (1 a 999). Para obter o valor do dígito verificador utilize a função calculadaVerificador.
Protótipo da função: def calculaVerificador(num)'''


def calculaVerificador(num):

    soma = 0 #inicializa a soma
    peso = 2 # inicializa o peso
    aux = num # inicializa a variavel aux com o valor de num. Vai ser utilizada para obter cada algarismo
    while True:
        aux1 = aux%10 # obtem o 1º digito mais à direita (unidades)
        soma += aux1* peso # multiplica-o pelo peso
        aux = aux//10 # obtem o numero restante sem o digito mais à direita
        peso += 1   # incrementa o peso
        if aux == 0:  # se já tivermos chegado ao fim do numero, termina o ciclo
            break
    resto_divisao = soma % 11  # calculo do resto da dicisão por 11
    valor = 11 - resto_divisao #  digito verificador
    if valor == 10 or valor == 11:
        valor = 0
    return valor

while True:
    numero = int(input('Introduza o numero para calculo do digito verificador (0 ou negativo para sair): '))
    if numero > 0:
        print('Digito Verificador: ',calculaVerificador(numero))
    else:
        break
