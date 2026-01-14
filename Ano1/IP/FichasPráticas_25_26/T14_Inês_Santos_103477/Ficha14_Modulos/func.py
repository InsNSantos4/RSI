# Modulo de funções

def soma(N):
    if N ==1:
        return 1
    if N > 0:
        resultado = N + soma(N-1)
        return resultado
    else:
        return 'Inserido Valor Inválido'

def soma_dig(N):
    if N ==0:
        return 0
    if N > 0:
        dig = N % 10
        novo_num = N//10
        resultado = dig + soma_dig(novo_num)
        return resultado


def fatorial(N):
    if N ==0:
        return 1
    if N > 0:
        resultado = N  * fatorial(N-1)
        return resultado

def conv_bin(n):
    b = ""
    if n > 0:
        b = conv_bin(n // 2) + str(n % 2)
    return b
