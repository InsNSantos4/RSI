# Escreva um procedimento que aceite como parâmetro um número inteiro positivo e
# imprima no ecrã a respetiva tabuada.
# Caso o valor recebido como parâmetro seja inválido (<=0 ou > 100), o procedimento
# deverá imprimir no ecrã a mensagem “Número inválido!”.
# Implemente um programa que leia do utilizador sucessivos números, fornecendo para
# cada um deles a respetiva tabuada utilizando o procedimento elaborado.
# O programa termina quando o utilizador introduz o número zero.

def tabuada_int(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

num_int = int(input("Introduza um número inteiro positivo: "))

while 1: # ou while True: 
    if(num_int < 0 or num_int > 100):
        print("Erro: número introduzido tem que ser inteiro e positivo.")
        print("\n")
        num_int = int(input("Introduza um número inteiro positivo: "))
    elif num_int == 0:
        print("Programa terminado.")
        break
    else:
        tabuada_int(num_int)
        num_int = int(input("Introduza um número inteiro positivo: "))