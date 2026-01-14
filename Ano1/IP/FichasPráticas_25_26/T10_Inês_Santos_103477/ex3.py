# Desenvolva uma função que permita calcular o índice de massa corporal (IMC) de um
# dado indivíduo. A função deve aceitar como parâmetros a altura (em metros) e o peso
# (em kg).
# Protótipo da função: def imc(altura, peso)
# NOTA: IMC = massa / altura**2

# Implemente outra função que permita obter a classificação da situação do individuo de
# acordo com a tabela seguinte:
# IMC Situação
# Inferior a 18.5 Abaixo do peso ideal
# Superior ou igual a 18.5 e inferior a 25 Peso ideal
# Superior ou igual a 25 e inferior a 30 Acima do peso ideal
# Superior ou igual a 30 Obeso
# Protótipo da função: def situação(imc)

def imc(altura, massa):
    return massa / altura**2

def situation(imc):
    if imc < 18.5:
        situation_message = "Abaixo do peso ideal."
    elif (imc >= 18.5 and imc < 25):
        situation_message ="Peso ideal."
    elif (imc >= 25 and imc < 30):
        situation_message ="Acima do peso ideal."
    elif imc >= 30:
        situation_message ="Obeso."
    return situation_message

while True:
    print("\n")
    print("*****************")
    print("Menu:")
    print("1. Calcular IMC")
    print("2. Sair")
    print("*****************")
    
    op = int(input("Escolha uma das opções: "))    
    
    if(op == 1):    
        hight_meters = float(input("Introduza a sua altura, em metros: "))
        weight_kg = float(input("Introduza o seu peso, em kg: "))
        
        imc_result =imc(hight_meters, weight_kg)
        print(f"IMC: {imc_result:.2f}")
        imc_situation = situation(imc_result)
        print("Situação IMC: "+ imc_situation)
        
    elif op == 2:
        print("Saiu do programa.")
        break
    else:
        print("Opção inválida")
        print("\n")