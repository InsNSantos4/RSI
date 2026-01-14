# Soma dos números naturais
# Escreva um programa que calcule a soma dos N primeiros números naturais, sendo N
# fornecido pelo utilizador. Proceda à respetiva validação dos dados de entrada.

n = int(input("Introduza um número: "))
print("\n")

soma = 0
i = 1

print ("Soma dos "+ str(n) + " primeiros números naturais: ")

if n > 0:
    while i <= n:
        soma = soma + i
        i = i + 1
    print(soma)
else:
    print("Erro: Número inserido não é um número natural.")