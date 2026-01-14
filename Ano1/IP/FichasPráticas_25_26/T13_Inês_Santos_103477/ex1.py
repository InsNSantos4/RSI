# Crie um programa que trate a exceção criada pela execução do seguinte código:

numerator = 10
denominator = 0

try:
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Erro: Não é possível divisão por zero.")