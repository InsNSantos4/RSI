# Crie um programa que trate a exceção criada pela execução do seguinte código:

num = input("Enter a number: ")
# Porque input() devolve sempre uma string, e não se pode fazer "texto" + 1
try:
    print(num + 1)
except TypeError:
    print("Erro: tipos incompatíveis na operação.")

# resolução copilot 
try:
    num = input("Enter a number: ")
    num = int(num)   # converter para inteiro
    print(num + 1)
except ValueError:
    print("Erro: deve introduzir um número válido.")
except TypeError:
    print("Erro: tipos incompatíveis na operação.")