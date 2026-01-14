# Ficha 6 Ex 02
# pop


## . Soma Par-Ímpar de Algarismos
# Para um número não-negativo N, define-se a soma par-ímpar de algarismos S(N) como a
# soma dos algarismos ímpares acrescido do dobro dos algarismos pares.
# Por exemplo,
# S(7) = 7
# S(362) = 3 + 2 ∗ 6 + 2 ∗ 2 = 19
# Escrever um programa que, dado um número N, determine a sua soma par-ímpar.

print("Soma Par-Ímpar de Algarismos  S(N)")
valor = int(input("Introduza o numero (N):"))

soma = 0
aux= valor

while aux > 0:
    dig = aux%10
    aux = aux//10

    if dig % 2 == 0: # digito par
        soma = soma +2*dig
    else:  # digito impar
        soma = soma + dig


print(f"Soma par-impar S({valor}) = {soma}")

#fim