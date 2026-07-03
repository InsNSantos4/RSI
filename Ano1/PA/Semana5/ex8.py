from Celsius import Celsius

# Mais testes:

temp_celsius = Celsius(21)

print(f"Aceder ao atributo (agora property) temperatura\nTemperatura: {temp_celsius.temperatura}\n")
#print(f"Tente aceder ao atributo __temperatura\n __temperatura: {temp_celsius.__temperatura}\n")

print(f"Tente outra vez... (dê uma olhadela ao campo __dict__ do objecto)\n__dict__ : {temp_celsius.__dict__}\n")
print(f"Tente aceder ao método privado criado anteriormente (ponto 7)\n__grauString(): {temp_celsius.__grauString()}")