#
# POP novembro 2022
#
# IP Ficha 07 Exercício 13
# pedrotomesa@ua.pt - RSI 2022-2023
# pop@ua.pt - SC
#
# 13. Escreva um programa que receba uma cadeia de caracteres representando números na
# base 2, base 8 ou base 16. O programa deve verificar se o número é válido e calcular o
# número correspondente em base 10. Por exemplo: 0xff em base 16 corresponde a 255
# em base 10, 017 em base 8 corresponde a 15 em base 10 e 101 em base 2 corresponde a
# 5 em base 10.


print("\n»»»»»»          Ficha 07  Exercicio 13")
print("\n»»»»»» ")
print("»»»»»»  Este programa recebe uma cadeia de caracteres representando números na base 2"
      ", base 8 ou base 16.")
print("»»»»»»  e converte para a base 10 ")
print("»»»»»»\n ")
print("\n")


def conversao(z):


    # determinar e validar a base da cadeia:
    Cadeia = z
    base = base1 = base2 = ""
    Valido = False
    Check = False
    Cadeia = Cadeia.upper()
    Num_D = Num_D1 = Num_D2 = -1
    l_Cadeia = len(Cadeia)

    if l_Cadeia > 2:
        Pref = Cadeia[0:2]
        if Pref == "0X":
            # Hex
            base = "Hex"
            Valido = True
            Num_H = Cadeia[2:len(Cadeia)]
            for i in Num_H:
                if not (i in "0123456789ABCDEF"):
                    Check = True
                    Valido = False
                    break
            if Valido:
                Check = True
                Num_D = int(Num_H, 16)

        elif Pref == "0O":
            # Oct
            base = "Oct"
            Valido = True
            Num_O = Cadeia[2:len(Cadeia)]
            for i in Num_O:
                if not (i in "01234567"):
                    Check = True
                    Valido = False
                    break
            if Valido:
                Check = True
                Num_D = int(Num_O, 8)  # Oct

        elif Pref == "0B":
            # Bin
            base = "Bin"
            Valido = True
            Num_B = Cadeia[2:len(Cadeia)]
            for i in Num_B:
                if not (i in "01"):
                    Check = True
                    Valido = False
                    break
            if Valido:
                Check = True
                Num_D = int(Num_B, 2)  # Bin

    # Cadeia sem prefixo de base
    while not Check:
        # bin
        Num_B = Cadeia[0:len(Cadeia)]
        Valido = True
        for i in Num_B:
            if not (i in "01"):
                Valido = False
                break
        if Valido:
            Check = True
            base = "Bin"
            Num_D = int(Num_B, 2)  # Bin
            base1 = "Oct"
            Num_D1 = int(Num_B, 8)  # Oct
            base2 = "Hex"
            Num_D2 = int(Num_B, 16)  # Hex
            continue

        # Oct
        Num_O = Cadeia[0:len(Cadeia)]
        Valido = True
        for i in Num_O:
            if not (i in "01234567"):
                Valido = False
                break
        if Valido:
            Check = True
            base = "Oct"
            Num_D = int(Num_B, 8)  # Oct
            base1 = "Hex"
            Num_D1 = int(Num_B, 16)  # Hex
            continue

        # Hex
        Num_H = Cadeia[0:len(Cadeia)]
        Valido = True
        for i in Num_H:
            if not (i in "0123456789ABCDEF"):
                Check = True
                Valido = False
                break
        if Valido:
            Check = True
            base = "Hex"
            Num_D = int(Num_O, 16)  # Hex
            continue

        Check = True

    # print("Valido:", Valido)
    # print("Check:", Check)

    if Valido:
        print("   Base:", base)
        print("   Decimal:", Num_D)

        if base1 != "":
            print()
            print("   Base:", base1)
            print("   Decimal:", Num_D1)

        if base2 != "":
            print()
            print("   Base:", base2)
            print("   Decimal:", Num_D2)
    else:
        print(" Valor inserido não é válido em Hexadecimal, Octal ou Binário")




while True:
    # Ler Cadeia com validação
    print()
    c = input("Entre a cadeia de carateres (X para sair): ")
    if c.upper() == "X":
        break
    if len(c) >= 1:
        conversao(c)
        print()
        input('==> Prima "ENTER" para continuar <==')
        continue
    print("»»»»»» A cadeia de carateres tem que ter pelo menos 1 carateres ")
