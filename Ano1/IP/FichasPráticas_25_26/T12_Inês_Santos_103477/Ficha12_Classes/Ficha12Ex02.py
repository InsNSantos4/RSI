# Ficha12 Ex2

#Crie uma Classe Quadrado que modele um quadrado, contendo os seguintes atributes e métodos:
#• Atributos: Tamanho do lado
#• Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    '''Modela um quadrado, contendo os seguintes atributes e métodos:
        • Atributos: Tamanho do lado
        • Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

    def __init__(self,lado):
        self.lado = lado

    def retLado(self):
        return self.lado

    def area(self):
        return self.lado**2

    def alteraLado(self,l):
        self.lado= l
        return self

q0=Quadrado()
q1 = Quadrado(2)

print('Lado=',q1.retLado())
print('Area=',q1.area())




q1.alteraLado(5)
print('Lado=',q1.retLado())
print('Area=',q1.area())


