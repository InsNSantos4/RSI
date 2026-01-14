# Fatorial
# b) Altere o programa de modo a que este permita calcular o fatorial de todos os números
# entre 1 e N, sendo N um número inteiro positivo fornecido pelo utilizador.
# Exemplo da saída de dados:
# O fatorial de 1 é 1
# O fatorial de 2 é 2
# O fatorial de 3 é 6

n = int(input("Introduza um número inteiro positivo: "))
print("\n")

print("O fatorial de todos os números entre 1 e " + str(n)+ " é: ")

if n > 0:
    while n > 0:
        fatorial = 1
        m = n
        while m > 0:
            fatorial = fatorial * m
            m = m - 1
        print("O fatorial de " + str(n) + " é "+ str(fatorial))
        n = n - 1
else:
    print("Erro: Número inserido não é um número inteiro positivo.")

# OU

# i = 1
# 
# while i <= n:
#         fatorial = 1
#         m = i
#         while m > 0:
#             fatorial = fatorial * m
#             m = m - 1
#         print("o fatorial de " + str(n) + " é "+ str(fatorial))
#
#         i = i+1