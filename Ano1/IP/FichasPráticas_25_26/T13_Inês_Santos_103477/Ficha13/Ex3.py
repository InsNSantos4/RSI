num=input('Digite um numero: ')
try:
    print(num+1)
except TypeError:
    print('valor inválido')