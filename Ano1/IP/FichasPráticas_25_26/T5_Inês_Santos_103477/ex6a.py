# Fatorial
# a) Escreva um programa que permita calcular o fatorial de um número N inteiro positivo,
# fornecido pelo utilizador. Proceda à respetiva validação dos dados de entrada.

n = int(input("Introduza um número inteiro positivo: "))
print("\n")

print("O fatorial de " + str(n)+ " é: ")

if n > 0:    
    fatorial = 1
    
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
else:
    print("Erro: Número inserido não é um número inteiro positivo.")