# Ficha 6 Ex 07
# POP

# Faça um programa que peça vários números ao utilizador. Uma vez efetuadas todas as
# leituras, deve apresentar o maior, o menor e a média de todos os números lidos, exceto o negativo.
# Exemplo:
#  Introduza um valor: 1
#  Introduza um valor: 7
#  Introduza um valor: 5
#  Introduza um valor: 23
#  Introduza um valor: -1
#    Maior = 23
#    Menor = 1
#    Média = 9.0

print("Calculo da média, maior e menor dos números positivos lidos.  ")

soma = 0
cont = 0
maior = float('-inf') # inicializa maior com - infinito (assim qualquer valor introduzido é assumido como o maior)
menor = float('inf') # inicializa menor com + infinito (assim qualquer valor introduzido é assumido como o menor)
while True:
    valor =int(input("Introduza um numero (negativo para terminar): "))
    if valor < 0:
        break
    cont += 1
#    if cont == 1:
#        maior = valor
#        menor = valor

    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma += valor

if cont > 0:
    print(f" Lidos {cont} numeros válidos")
    print(f"  Maior: {maior}")
    print(f"  Menor: {menor}")
    print(f"  Média: {soma/cont:.2f}")
