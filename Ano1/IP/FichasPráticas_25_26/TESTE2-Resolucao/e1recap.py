def soma_primos(n):
    primos = [2, 3, 5, 7]
    soma = sum(int(digito) for digito in str(n) if int(digito) in primos)
    return soma

n = int(input("Digite um numero: "))
print(f"A soma dos numeros primos do numero que deu foi {soma_primos(n)}")