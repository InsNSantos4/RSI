# Ficha 10 Ex02

'''Escreva um procedimento que aceite como parâmetro um número inteiro positivo
e imprima no ecrã a respetiva tabuada.
Caso o valor recebido como parâmetro seja inválido (<=0 ou > 10),
o procedimento deverá imprimir no ecrã a mensagem “Número inválido!”.
Implemente um programa que leia do utilizador sucessivos números,
fornecendo para cada um deles a respetiva tabuada utilizando o procedimento elaborado.
O programa termina quando o utilizador introduz o número zero.'''

def tabuada(numero):
        if 0 < numero <= 100:
            for i in range(1,11):
                print(f'{i:2} x {numero:3} = {i*numero:4}')
            print()
        else:
            print ('>>>> Número inválido <<<<\n ')

while True:
    n = input('Calculo da Tabuada. \nInsira um nº de 1 a 100  (0 para terminar): ')
    if n == '0':
        print('--->  Fim! ')
        break
    elif n.isdigit(): # True se todos os caracteres são digitos
        tabuada(int(n))
    else:
        print('>>> Valor inválido <<<\n')