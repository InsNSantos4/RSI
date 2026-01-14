# Ficha 8 Ex 05

# Euromilhões  10 apostas
#import random

#   n=random.randint(inicio,fim)

print('Euromilhões: \n Introduzir as apostas: \n 5 numeros de 1 a 50 e 2 estrelas de 1 a 12'
      ' no formato n,n,n,n,n,e,e  (ex: 22,23,32,40,50,6,12)')
print()

n_apostas = int(input(' Quantas apostas deseja?: '))

ap=[]
for i in range(n_apostas):
    ap_in = input(f' Aposta {i+1}: ')
    ap_list =ap_in.split(',')
    ap.append(ap_list)
print(ap)

# chave
ch=input(' Introduza a chave: ')
chave = ch.split(',')

print(f'Chave: {chave} ')



for i in range(n_apostas):
    count_n = 0
    count_s = 0
    str_chave =''
    str_star = ''
    print(f' Aposta {i+1}: {ap[i]} ')
    for n in ap[i][:5]:
        if n in chave[:5]:
            count_n += 1
            str_chave  += str(n)  + ' '
    for s in ap[i][5:]:
        if s in chave[5:]:
            count_s += 1
            str_star  += str(s)  + ' '

    print(f'    Acertos:   Numeros: {count_n} ({str_chave})  Estrelas: {count_s} ({str_star}) ',end='' )

    if   count_n == 5 and count_s == 2:
        print(' 1º prémio')
    elif count_n == 5 and count_s == 1:
        print(' 2º prémio')
    elif count_n == 5 and count_s == 0:
        print(' 3º prémio')
    elif count_n == 4 and count_s == 2:
        print(' 4º prémio')
    elif count_n == 4 and count_s == 1:
        print(' 5º prémio')
    elif count_n == 3 and count_s == 2:
        print(' 6º prémio')
    elif count_n == 4 and count_s == 0:
        print(' 7º prémio')
    elif count_n == 2 and count_s == 2:
        print(' 8º prémio')
    elif count_n == 3 and count_s == 1:
        print(' 9º prémio')
    elif count_n == 3 and count_s == 0:
        print('10º prémio')
    elif count_n == 1 and count_s == 2:
        print('11º prémio')
    elif count_n == 2 and count_s == 1:
        print('12º prémio')
    elif count_n == 2 and count_s == 0:
        print(' 13º prémio')
    else :
        print(' Sem prémio')
