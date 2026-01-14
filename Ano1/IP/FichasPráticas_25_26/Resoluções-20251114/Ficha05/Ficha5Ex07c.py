# Ficha 5 Ex 07a
# POP 2023

# Encontra os numeros primos gémeos até N (que diferem apenas em duas unidades)

print("Este programa Encontra os numeros primos gémeos até N ")

N = int(input("Introduza um numero inteiro positivo N: "))

primo_anterior = 2 #
for m in range(2,N+1) :
    # verificar se é primo
    primo = True

    for i in range(2,int(m/2)+1):
        if m %i == 0:
            primo = False
            break

    if primo == True:
        dif = (m - primo_anterior)
        if dif == 2:
            print(f" {primo_anterior:5} e {m:5} são numeros primos gémeos")
        primo_anterior = m

#fim do programa