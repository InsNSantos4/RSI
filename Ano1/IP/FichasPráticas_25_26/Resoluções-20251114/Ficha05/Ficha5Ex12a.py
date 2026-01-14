# POP 2023
# Ficha 05 ex 12a

# Pirâmide de Numeros
# Escreva um programa que Implemente um programa que imprima no ecrã a seguinte pirâmide de números:
#       1
#      121
#     12321
#    1234321
#   123454321

print('Pirâmide de de Numeros ')
n = 5

for i in range(1,6):  # uma iteração por linha

    print(" "*(5-i),end="" ) # print dos brancos sem mudar de linha

    for j in range(1,i+1): # print dos numeros em crescendo sem mudar de linha
        print(j,end="")

    for l in range(j-1,0,-1):  # print dos numeros em decrescente sem mudar de linha
        print(l,end="")

    print() # mudança de linha
#fim

