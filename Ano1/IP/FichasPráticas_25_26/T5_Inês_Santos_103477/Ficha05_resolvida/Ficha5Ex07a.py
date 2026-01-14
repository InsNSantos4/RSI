# Ficha 5 Ex 07a
# POP 2023

# Verifica se N é primo

print("Este programa verifica se o numero introduzido é primo")

N = int(input("Introduza um numero inteiro positivo: "))

primo = True

for i in range(2,int(N/2)+1):
    if N %i == 0:
        primo = False
        break

if primo:   # primo == True
    print(f"{N} é numero primo")
else:
    print(f"{N} NÃO é numero primo, é divisivel por {i}")

#fim do programa