# Ficha 5 Ex 07b
# POP 2023

# Encontra os numeros primos até N

print("Este programa Encontra os numeros primos até N ")

N = int(input("Introduza um numero inteiro positivo N: "))


for m in range(2,N+1) :
    primo = True
    for i in range(2,int(m/2)+1):
        if m %i == 0:
            primo = False
            break

    if primo == True:  # bastava -- if primo:  -- pois primo já é boolean
        print(f"{m:5} é numero primo")


#fim do programa