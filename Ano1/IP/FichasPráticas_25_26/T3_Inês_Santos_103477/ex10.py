# Maior de dois números
# 10. Escreva um programa que leia dois números e indique o maior deles. O programa deverá
# contemplar a situação dos dois números serem iguais.

print("Insert two numbers ...")
print ("\n")

num1 = float(input("First number: "))
print ("\n")
num2 = float(input("Second number: "))
print('\n')

if num1 == num2:
    print("The two numbers are the same.")
elif num1 > num2:
    print(str(num1)+" is the higher of the two numbers.")
else:
    print(str(num2)+" is the higher of the two numbers.")