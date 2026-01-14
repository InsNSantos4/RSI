#
# POP novembro 2022
#
# IP Ficha 07 Exercício 13 B
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
print("»»»»»»   e converte para a base 10 (testa a validade nas três bases")
print('»»»»»»  Nota: Os prefixos "0x", "0o" e "0b" são opcionais ')
print("»»»»»»\n ")

def conversao(z):

    Cadeia = z
    base = base1 = base2 = ""
    Valido = False
    Cadeia = Cadeia.upper()
    Num_D = Num_D1 = Num_D2 = -1

    # Hexadecimal
    try:
        Num_D = int(Cadeia, 16)
        base = "Hex"
        Valido = True
    except ValueError:
            pass
            # cadeia não é valida em Hexadecimal

    # Octal
    try:
        Num_D1 = int(Cadeia, 8)
        if not Valido:
            base = "Octo"
            Num_D = Num_D1
            Num_D1 = -1

        else:
            base1 = "Octo"
        Valido = True
    except ValueError:
            pass
            # cadeia não é valida em Octal

    # Binario
    try:
        Num_D2 = int(Cadeia, 2)
        if base == "":
            Num_D = Num_D2
            Num_D2 = - 1
            base = "Bin"
        elif base1 == "":
            Num_D1 = Num_D2
            Num_D2 = - 1
            base1 = "Bin"
        else:
            base2 = "Bin"
        Valido = True
    except ValueError:
        pass
        # cadeia não é valida em binario



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
