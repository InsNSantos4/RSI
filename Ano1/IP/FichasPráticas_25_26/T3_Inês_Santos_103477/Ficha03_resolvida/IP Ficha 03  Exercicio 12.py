#
# POP Setembro 2022
#
# IP Ficha 03  Exercicio 12
#
# Calculadora
# 12. Escreva um programa (Calculadora) que leia dois operandos reais e o símbolo da
# operação, e que apresente o respetivo resultado.
# A entrada de dados deve ser organizada como se indica abaixo:
# operando 1? ...
# operação? ...
# operando 2? ...
# operações contempladas no programa:
# operação Símbolo
# adição +
# subtração –
# multiplicação *
# divisão /


print("\n»»»»»» ")
print("»»»»»»  Este programa (Calculadora) lê dois operandos reais,")
print("»»»»»»  lê o símbolo da operação e apresenta o respetivo resultado.")
print("»»»»»»\n ")

# Ler os operandos
num_1 = float(input("Qual o operando 1?: "))
num_2 = float(input("Qual o operando 2?: "))

# Ler a operação
oper = input("Escolha a operação (+,-,/,*) ?: ")

expressao = "Resultado: "+str(num_1)+oper+str(num_2)+ " = "

# SOMA
if oper == "+":  # SOMA
    print(expressao, num_1 + num_2)

# SUBTRAÇÃO
elif oper == "-":
    print(expressao, num_1 - num_2)

# MULTIPLICAÇÃO
elif oper == "*":
    print(expressao, num_1 * num_2)

# DIVISÃO
elif oper == "/":
    if num_2 != 0:  # divisor diferente de zero
        print(expressao, num_1 / num_2)
    else:  # divisor igual a zero
        print("Divisão inválida:", num_1, oper, num_2, ", divisor não pode ser zero")

# operador diferente das opções válidas
else:
    print("Operador ", oper, " é inválido. Os operadores válidos são + ou - ou / ou * ")


# fim do programa