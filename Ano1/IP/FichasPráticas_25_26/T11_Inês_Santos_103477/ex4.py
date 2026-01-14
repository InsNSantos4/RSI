# Escreva uma função recursiva que aceite um inteiro decimal e exiba o seu equivalente em binário.

def decimal_to_binary(decimal_num):
    #caso base:
    if decimal_num == 0 or decimal_num == 1:
        return str(decimal_num)
    else:
        # binário da parte inteira da divisão por 2 + resto da divisão por 2
        return decimal_to_binary(decimal_num // 2) + str(decimal_num % 2)

num = int(input("Introduza um número decimal: "))

while num < 0:
    num = int(input("Introduza um número válido (>= 0): "))
    
print(f"{num} em binário é {decimal_to_binary(num)}.")
