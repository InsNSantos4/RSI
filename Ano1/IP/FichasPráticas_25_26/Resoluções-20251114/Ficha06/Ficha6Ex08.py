# Ficha 6 Ex 08
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

print("Verificação se 2 numeros sáo amigos ( soma dos divisores de qualquer deles, incluindo a \n"
      "unidade e excluindo o próprio número, for igual ao outro número)")

numero1 = int(input("Introduza o 1º número: "))
numero2 = int(input("Introduza o 2º número: "))

# divisores de numero1
div_numero1 = ""  # divisores de n
soma_divisores_n1 = 0  # soma dos divisores do numero1

for i in range(1, int(numero1  / 2) + 1): # só é necessário procurar até metade do valor
    if numero1  % i == 0:
        soma_divisores_n1 = soma_divisores_n1 + i
        div_numero1 = div_numero1 + " " + str(i)

# divisores de numero2
div_numero2 = ""  # divisores de numero2
soma_divisores_n2 = 0  # soma dos divisores do numero1

for i in range(1, int(numero2 / 2) + 1):
    if numero2  % i == 0:
        soma_divisores_n2 = soma_divisores_n2 + i
        div_numero2 = div_numero2 + " " + str(i)

print(f"Soma dos Divisores de {numero1}: {soma_divisores_n1}  Divisores: {div_numero1}")
print(f"Soma dos Divisores de {numero2}: {soma_divisores_n2}  Divisores: {div_numero2}")

if numero1 == soma_divisores_n2 and numero2 == soma_divisores_n1 :
    print(f" {numero1} e {numero2} são amigos")
else:
    print(f" {numero1} e {numero2} não são amigos")

#fim