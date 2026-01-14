# Ficha 6 Ex 08a
# POP

# Dois números dizem-se amigos se a soma dos divisores de qualquer deles, incluindo a
# unidade e excluindo o próprio número, for igual ao outro número.
# Desenvolva um algoritmo que permita verificar se dois números m e n são números
# amigos.
# Por exemplo, 220 e 284 são números amigos.
# Divisores de 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
# Soma: 284
# Divisores de 284: 1, 2, 4, 71, 142
# Soma: 220

print("Identificação dos numeros amigos até M ( soma dos divisores de qualquer deles, incluindo a \n"
      "unidade e excluindo o próprio número, for igual ao outro número)")

m = int(input("Introduza o M: "))

for j in range(1,m+1):

    print(f'\rCalculo da soma de divisores de {j}',end="")
    # divisores de m
    dm = ""  # divisores de m
    sdm = 0  # soma dos divisores de m
    for i in range(1, int(j)):
        if j % i == 0:
            sdm = sdm + i
            dm = dm + " " + str(i)
    #print(f"Soma dos Divisores de {j}: {sdm}  Divisores: {dm}")
    for l in range (1,j+1):   # divisores de n
        dn = ""  # divisores de n
        sdn = 0  # soma dos divisores de n
        for k in range(1, int(l )):
             if l % k == 0:
                sdn = sdn + k
                dn = dn + " " + str(k)
        #print(f"     Soma dos Divisores de {l}: {sdn}  Divisores: {dn}")
        if sdn == j and sdm == l and j!=l:
            print(f"\n {j} e {l} são amigos")
            print(f"Soma dos Divisores de {l}: {sdn}  Divisores: {dn}")
            print(f"Soma dos Divisores de {j}: {sdm}  Divisores: {dm}")

# fim


