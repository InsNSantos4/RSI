# par ou ímpar
# 6. escreva um programa que dado um número inteiro introduzido pelo utilizador indique se
# o número é, ou não, par.

num = int(input("Please insert a number: "))

if num % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")