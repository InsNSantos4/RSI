# POP 2023
# Ficha 05 ex 09b

#Jogo da Adivinha
# Escreva um programa que deverá deixar o utilizador adivinhar um número inteiro
# introduzido previamente.
# O# A cada tentativa o programa deverá indicar se o número é
# maior, menor ou se acertou no número. No caso de o utilizador acertar, o programa
# deve indicar quantas tentativas necessitou para tal.

# O utilizador deve também introduzir o nº máximo de tentativas

print('Jogo da Adivinha')
m = int(input('Introduza o valor que o utilizador tem que adivinhar: '))

while True:
    max = int(input('Introduza o valor maximo de tentativas: '))
    if max > 0:
        break
    else:
        print("==> O valor mmáximo de tentativas tem que ser maior que zero")



contador = 1

while contador <= max:
    n = int(input(f'Introduza o valor da {contador}a. tentativa:  '))
    if m == n:
        print(f'Parabéns acertou no numero {n} à {contador}a. tentativa:  ')
        break
    elif m < n:
        print(f' {contador}a. tentativa:  {n} é maior que o valor a adivinhar ')
    else:
        print(f' {contador}a. tentativa:  {n} é menor que o valor a adivinhar ')
    contador += 1
else:
    print(f'Lamento, atingiu o nº máximo de tentativas ({max})   ')

#fim

