# Ficha 6 Ex 04
# POP

# Soma dos Cubos
# Alguns números inteiros verificam uma regra em que o seu valor é igual à soma dos
# cubos dos seus algarismos.
# Por exemplo,
# 153 é igual a 1**3 + 5**3 + 3**3
# 24 não é igual a 2**3 + 4**3
# Implemente um programa que dado um número inteiro N determine se esse número é
# ou não igual à soma dos cubos dos seus algarismos.

print(" Soma dos Cubos:  verificação se o valor de um numero é igual à soma dos  cubos dos seus algarismos. ")
print("   Ex 153 = 1**3 + 5**3 + 3**3")
numero = int(input(" Introduza o numero a verificar: "))

soma = 0
aux = numero
while aux>0:
    alg = aux%10
    aux = aux//10
    soma = soma + alg**3


if numero == soma:
    print(f" Verifica-se a regra da Soma dos Cubos para o numero {numero}" )
else:
    print(f" Não se verifica a regra da Soma dos Cubos para o numero {numero}" )


#Fim

# cubos = "" # para printar 1**3 + 5**3 + 3**3
# cubos = " + " +str(alg)+"**3"+ cubos  # para printar 1**3 + 5**3 + 3**3
# print(f" {n} = {cubos}") # para printar 1**3 + 5**3 + 3**3
# print(f" {n} != {cubos}") # para printar 1**3 + 5**3 + 3**3