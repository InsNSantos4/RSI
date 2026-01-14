# Múltiplos de 3 entre m e M
# Implemente um programa que imprima no ecrã os múltiplos de 3 entre m e M, sendo m
# e M fornecidos pelo utilizador e em que m tem de ser inferior a M. Proceda à respetiva
# validação dos dados de entrada.

m = int(input("Introduza um número inteiro m: "))

M = int(input("Introduza um outro número inteiro M, superior ao anterior:"))

if(M > m):
    i = m
    while i <= M:
        if(i%3==0):
            print(i)
        i = i + 1
else:
    print("Erro: O segundo número introduzido não pode ser menor do que o primeiro.")