import ficha11

number = int(input("Introduza um número natural: "))

while number <= 0:
    number = int(input("Introduza um número natural (inteiro maior que zero): "))

print(f"A soma dos {number} primeiros números naturais é: {ficha11.soma_n(number)}.\n")




inteiro = int(input("Introduza um inteiro positivo: "))

while inteiro < 0:
    inteiro = int(input("Introduza um inteiro positivo válido: "))

print(f"A soma dos dígitos do número que inseriu ({inteiro}) é {ficha11.sum_digits(inteiro)}.\n")



inteiro = int(input("Introduza um inteiro positivo: "))

while inteiro < 0:
    inteiro = int(input("Introduza um inteiro positivo válido: "))
    
print(f"O fatorial de {inteiro} é {ficha11.fatorial(inteiro)}.\n")



num = int(input("Introduza um número decimal: "))

while num < 0:
    num = int(input("Introduza um número válido (>= 0): "))
    
print(f"{num} em binário é {ficha11.decimal_to_binary(num)}.\n")





# resolução copilot:
print("=== Testes ao módulo ficha11 ===")

n = int(input("Introduza N para soma dos primeiros N naturais: "))
print("Soma =", ficha11.soma_n(n))

num = int(input("\nIntroduza um número para somar os dígitos: "))
print("Soma dos dígitos =", ficha11.sum_digits(num))

f = int(input("\nIntroduza um número para calcular o fatorial: "))
print("Fatorial =", ficha11.fatorial(f))

d = int(input("\nIntroduza um número decimal para converter para binário: "))
print("Binário =", ficha11.decimal_to_binary(d))
