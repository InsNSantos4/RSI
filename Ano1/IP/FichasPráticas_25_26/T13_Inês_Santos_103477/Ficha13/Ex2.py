even_numbers=[2,4,6,8]

try:
    print(even_numbers[4])
except IndexError:
    print('Indice não existente - fora do intervalo')