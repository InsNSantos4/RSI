# POP 2023
# Ficha 05 ex 08

#Implemente um programa que permita calcular o máximo divisor comum – mdc(m,n)
# entre dois números inteiros positivos m e n fornecidos pelo utilizador

print('Este programa calcula o máximo divisor comum – mdc(m,n) entre dois números inteiros positivos m e n')

m = int(input('Introduza o valor de m: '))
n = int(input('Introduza o valor de n: '))

if m < n: # m tem que ser maior n
    m,n = n,m

# Calculo com ciclo for :

for i in range(n,0,-1): # teste decrescente a começar no mais pequeno
    if (m % i == 0) and (n % i == 0): # se m e n são divisiveis por i, então i é divisor comum
        print(f"Ciclo for   - Calculo do Máximo Divisor Comum entre {m} e {n}  MDC({m},{n}) = {i} ")
        break



# Calculo com ciclo while :
i = n
while i > 0: # teste decrescente a começar no mais pequeno
    if (m % i == 0) and (n % i == 0): # se m e n são divisiveis por i, então i é divisor comum
        print(f"Ciclo while - Calculo do Máximo Divisor Comum entre {m} e {n}  MDC({m},{n}) = {i} ")
        break
    i -= 1

