# Programa que receba 3 números e devolva qual o maior:

print("Introduza o primeiro de 3 números:")
first = float(input())
print("\n")

print("Introduza o segundo de 3 números:")
second = float(input())
print("\n")

print("Introduza o terceiro de 3 números:")
third = float(input())
print("\n")

if second > first:
    bigger_number = second
    if third > second:
        bigger_number = third
else:
    if third > first:
        bigger_number = third
    bigger_number = first
    
print("Maior número: " + str(bigger_number))