# Ficha 6 Ex 05
# POP

# Numeros por extenso:

n = int(input("Introduza um número inteiro a escrever por extenso, entre 0 e 99: "))

u = n % 10
d = n // 10
ex = 0
ex_d = ''
e= 'e '

if 0 <= n <= 99 :
    if n ==0 :
        ex = 'zero'
    elif n == 10:
        ex = 'dez'
    elif n == 11:
        ex = 'onze'
    elif n == 12:
        ex = 'doze'
    elif n == 13:
        ex = 'treze'
    elif n == 14:
        ex = 'catorze'
    elif n == 15:
        ex = 'quinze'
    elif n == 16:
        ex = 'dezasseis'
    elif n == 17:
        ex = 'dezassete'
    elif n == 18:
        ex = 'dezoito'
    elif n == 19:
        ex = '19'

    # unidades
    elif u == 0:
        ex = ''
    elif u == 1:
        ex = 'um'
    elif u == 2:
        ex = 'dois'
    elif u == 3:
        ex = 'três'
    elif u == 4:
        ex = 'quatro'
    elif u == 5:
        ex = 'cinco'
    elif u == 6:
        ex = 'seis'
    elif u == 7:
        ex = 'sete'
    elif u == 8:
        ex = 'oito'
    elif u == 9:
        ex = 'nove'

    # dezenas
if 2 <= d <=9:
    if d == 2:
        ex_d = 'vinte'
    elif d == 3:
        ex_d = 'trinta'
    elif d == 4:
        ex_d = 'quarenta'
    elif d == 5:
        ex_d = 'cinquenta'
    elif d == 6:
        ex_d = 'sessenta'
    elif d == 7:
        ex_d = 'setenta'
    elif d == 8:
        ex_d = 'oitenta'
    elif d == 9:
        ex_d = 'noventa'


if ex == 0:
    print('Numero inválido')
else:
    print(f"Numero por extenso: {ex_d} {e*(u!=0 and n>20)}{ex}")