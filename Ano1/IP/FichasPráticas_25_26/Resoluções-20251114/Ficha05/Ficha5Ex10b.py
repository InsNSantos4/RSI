# POP 2023
# Ficha 05 ex 10b

# Dígitos de um número
# Escreva um programa que dado um número inteiro fornecido pelo utilizador,
# calcule o número de vezes que surge o algarismo zero nesse número e
# forneça também a indicação da posição dos mesmos.

print('Dígitos de um número - algarismos zero desse número')
n = int(input('Introduza o numero a analisar: '))
contador = 0
aux = n
n_alg = 0

while True:
    u = aux % 10 # obtem o digito mais à direita (unidades)
    n_alg += 1
    if u == 0: # se for igual a zero, incrementa o contador
        contador += 1
        print(f'Encontrado um zero na posição {n_alg}')
    aux = aux // 10 # obtem o numero sem o digito da direita
    if aux == 0: # se já não há mais digitos, termina
        break
print(f'\nO nº{n} tem {contador} zeros')

#fim

