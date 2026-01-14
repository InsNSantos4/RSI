#  Programa que identifique se um número é ímpar ou par

print("Introduza um número:")
n = int(input())
print("\n")

if(n%2 == 0):
    print("Número par.")
    
if(n%2 != 0):
    print("Número ímpar.")