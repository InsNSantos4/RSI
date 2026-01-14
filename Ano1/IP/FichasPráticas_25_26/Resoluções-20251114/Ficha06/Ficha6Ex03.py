# Ficha 6 Ex 03
# pop

# Conversor Decimal Binário
# Num sistema digital, como um PC por exemplo, toda a informação é representada
#  utilizando o sistema binário. Neste sistema só são utilizados os algarismos zero (0) e um
#  (1). Significa isto que os números escritos utilizando o sistema decimal (12, 23, 403, ...)
#  são convertidos numa sequência de zeros e uns.
#  Por exemplo, o valor decimal 22(10) é convertido em binário por 10110(2)

print("Conversor Decimal Binário")
a = int(input("Introduza o numero Decimal para converter em Binário: "))

bin = ""
aux= a
while True:
    dig = aux%2
    num = aux//2

    bin = str(dig)+bin

    if num == 0:
        break
    aux = num

print(f"Representação Binaria do decimal {a}  = {bin}")

#fim