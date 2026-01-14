#Ficha14Ex01
import func



numero = int(input('Calculo da soma dos N primeiros numeros naturais \nEntre o valor de N: '))
print('\nSoma :',func.soma(numero))


numero = int(input('Calculo da soma dos algarismos de um numero:\nEntre o valor de N: '))
print('\nSoma :',func.soma_dig(numero))


numero = int(input('Calculo do Fatorial (N!) de um numero:\nEntre o valor de N: '))
print('\nFatorial :',func.fatorial(numero))

numero = int(input('Conversão de numero N, base 10 para binário:\nEntre o valor de N: '))
print('\nBinãrio :',func.conv_bin(numero))