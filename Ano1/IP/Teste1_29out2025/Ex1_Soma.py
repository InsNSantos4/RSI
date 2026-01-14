# 103477 Inês Nunes Santos

n = int(input("Introduza um número inteiro positivo: "))

if n <= 0:
    print("Valor não válido")
else:
    soma = 0
    for i in range(1, n+1):
        if(i % 2 == 0):
            soma += i
    print(soma)
