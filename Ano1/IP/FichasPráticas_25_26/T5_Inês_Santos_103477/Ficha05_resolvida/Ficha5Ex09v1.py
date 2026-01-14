#
# POP outubro 2022
#
# IP Ficha 05  Exercicio 09
#
# 9. Jogo da adivinha
# a) Escreva um programa que deverá deixar o utilizador adivinhar um número inteiro
# introduzido previamente. A cada tentativa o programa deverá indicar se o número é
# maior, menor ou se acertou no número. No caso de o utilizador acertar, o programa
# deve indicar quantas tentativas necessitou para tal.
# b) Altere o programa de modo a que seja possível controlar o número máximo de
# tentativas. O programa deverá pedir inicialmente esse valor, efetuando a respetiva
# validação de entrada.

print("\n»»»»»»          Ficha 05  Exercicio 09")
print("\n»»»»»» ")
print("»»»»»»  Este programa é um jogo de adivinha. ")
print("»»»»»»  O utilizador deve adivinhar um número secreto (entre 1 e 1000).")
print("»»»»»»  A cada tentativa é retornado se o valor é maior, menor ou se acertou no número")
print("»»»»»»\n ")
print("\n")

# geração de numero aleatório ente 1 e 1000
import random
Numero = random.randint(1, 1000)

# ler numeros de tentativas   t_max
while True:
    t1 = input(f"Entre o numero de tentativas permitido ( 0 para sem limite): ")
    if t1.isdigit():  # t1 é numerico
        t_max = int(t1)
        break
    print("»»»»»» tem que ser um número inteiro maior que 0")



t = 1 # inicialização do contador de tentativas
#leitura e teste do valor da tentativa
# só executa se o numero de tentativas não exceda o nº maximo ou se não há limite (t_max= 0)
while t <= t_max or t_max == 0: # só executa se o numero de tentativas não exceda o nº maximo ou se não há limite (t_max= 0)
    m1= input(f"Entre valor da {t} tentativa: ")
    if m1.isdigit():  # m é numerico
        m=int(m1)
        # valor entrado é numero. Execução do teste do valor entrado na tentativa
        if m == Numero:
            print(f"Parabens! Acertou no numero secreto {Numero} em {t} tentativas.")
            break  # acertou , sai do ciclo
        elif m > Numero:
            print(f"{m} é maior que o numero secreto")
            t += 1
            continue # falhou, volta ao inicio do ciclo
        elif m < Numero:
            print(f"{m} é menor que o numero secreto")
            t += 1
            continue # falhou, volta ao inicio do ciclo
    # se o programa chega aqui, é porque o valor entrado não é um numero inteiro positivo
    print("»»»»»» Deve ser um número inteiro positivo de 1 a 1000 ")
    # volta ao inicio do ciclo
else:
    # condição do while falhou.
    print(f"Excedeu o nº maximo ({t_max})  de tentativas. Numero secreto era {Numero}")




# fim do programa
