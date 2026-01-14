# 103477 Inês Nunes Santos

num_secreto = int(input("Número Secreto: "))
print("\n")

adivinhou = False
print("Tente adivinhar o número secreto...")
palpite = int(input("Introduza o seu palpite (número inteiro): "))

num_tentativas = 0

while adivinhou != True:
    num_tentativas += 1
    if(palpite == num_secreto):
        adivinhou = True
        if num_tentativas == 1:
            print("Parabéns! Adivinhou o número secreto em" , int(num_tentativas),"tentativa!")
        elif num_tentativas > 1:
            print("Parabéns! Adivinhou o número secreto em" , int(num_tentativas),"tentativas!")
    else:
        adivinhou = False
        palpite = int(input("Não adivinhou. Introduza o seu novo palpite (número inteiro): "))
