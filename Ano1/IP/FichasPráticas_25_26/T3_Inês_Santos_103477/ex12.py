# Calculadora
# 12. Escreva um programa (Calculadora) que leia dois operandos reais e o símbolo da
# operação, e que apresente o respetivo resultado.
# A entrada de dados deve ser organizada como se indica abaixo:
# Operando 1? ...
# Operação? ...
# Operando 2? ...
#
# Operações contempladas no programa:
# Operação               Símbolo
# adição                    +
# subtração                 –
# multiplicação             *
# divisão                   /

import sys
operand1 = float(input("Operando 1? "))
operation_symbol = str(input("Operação? "))
operand2 = float(input("Operando 2? "))

if (operation_symbol == '+'):
    result = operand1 + operand2
elif operation_symbol == '-':
    result = operand1 - operand2
elif operation_symbol == '*':
    result = operand1 * operand2
elif operation_symbol == '/':
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Can't divide by zero.")
        sys.exit(1)         # saída com erro
else:
    print("Operation not supported in this calculator.")
    sys.exit(1)             # saída com erro

# 0 indica saída com sucesso
    
print("Resultado: " + str(result))