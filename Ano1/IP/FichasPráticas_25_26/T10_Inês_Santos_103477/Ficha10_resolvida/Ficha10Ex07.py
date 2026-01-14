# Ficha 10 Ex07

import random

def numero_aleatorio(max):
    return random.randint(0,max)

def jogar(numero_maximo,maximo_de_tentativas):
    aleatorio = numero_aleatorio(numero_maximo)
    tentativa = 0
    while tentativa < maximo_de_tentativas:
        tentativa += 1
        guess = int(input(f'Introduza a sua {tentativa}ª tentativa: '))
        if guess > numero_maximo or guess < 0:
            print('Valor inválido')
            tentativa -= 1
        elif guess == aleatorio:
            print(f'Parabéns! acertou à {tentativa} tentativa')
            break
        elif guess > aleatorio:
            print(f'Valor superior ao numero secreto')
        elif guess < aleatorio:
            print(f'Valor inferior ao numero secreto')
    else:
        print(f'Excedeu o nº maximo de tentativas\n---> nº secreto: {aleatorio}')



#programa principal
print('** Adivinhe um numero gerado pelo programa **')
n_maximo = int(input('Introduza o valor maximo (inteiro): '))
max_tentativas =  int(input('Introduza o valor maximo de tentativas: '))

while True:
    jogar(n_maximo, max_tentativas)
    novo_jogo = input('\nQuer Jogar de novo?\n "0" para terminar. Outro caracter para novo jogo: ')
    if novo_jogo == '0':
        print('>> Fim!')
        break
