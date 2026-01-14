# Números pares entre 1 e N:
#
# Escreva um programa que apresente no ecrã os números pares entre 1 e N, sendo N um
# número inteiro positivo e fornecido pelo utilizador. Proceda à respetiva validação dos
# dados de entrada.

n = int(input("Introduza um número inteiro positivo: "))
print("\n")
print("Números pares entre 1 e " +  str(n) + ": ")

if n > 0:
    for i in range(2, n+1, 2):        
        print(i)
else:
    print("Número introduzido não é um inteiro positivo.")