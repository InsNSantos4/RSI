#
# POP novembro 2022
#
# IP Ficha 07 Exercício 13 c
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
    Valido = False
    resultado = []
    Base=[0]*17
    BaseA=[0]*17
    Base[2] = "Bin"
    Base[8] = "Oct"
    Base[16] = "Hex"
    BaseA[2] = "0b"
    BaseA[8] = "0o"
    BaseA[16] = "0x"
    Cadeia = z
    for i in (16,8,2):
        try:
            Num = int(Cadeia, i)
            aux = [Base[i],Num,BaseA[i]]
            resultado.append(aux)
            Valido = True
        except ValueError:
                pass
                # cadeia não é valida em Hexadecimal

    if Valido:
        print()
        Cadeia = Cadeia.strip()
        print("Valor entrado : ",Cadeia.upper())

        for i in range(len(resultado)):
            aux = resultado[i]
            val = Cadeia.upper()
            if len(val) >2:
                if aux[2].upper() == val[0:2]:
                    val = val[2:]
            print("    Base:", aux[0],aux[2]+val,end=" ")
            print("\t Decimal:", aux[1])
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
