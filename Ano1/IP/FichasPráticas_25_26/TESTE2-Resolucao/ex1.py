def soma_digitos_primos(numero):
    primos = [2, 3, 5, 7]
    #soma = sum(int(digito) for digito in str(numero) if int(digito) in primos)
    soma = 0
    for i in str(numero):
        if int(i) in primos:
            soma += int(i)
    return soma

# Exemplo de teste
numero = int(input("Digite um número: "))
print(f"A soma dos dígitos primos é: {soma_digitos_primos(numero)}")