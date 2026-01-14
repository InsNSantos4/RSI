# 103477 Inês Nunes Santos

email = input("Introduza o seu email do domínio principal da ua: ")

separated = email.split("@")

if separated[0].islower() and separated[1] == "ua.pt":
    print("VÁLIDO")
else:
    print("NÃO VÁLIDO")
