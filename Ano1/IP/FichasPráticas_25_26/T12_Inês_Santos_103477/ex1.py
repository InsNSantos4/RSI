# Crie uma Classe Bola que modele uma bola. A classe deverá conter os seguintes atributos
# e métodos:
# • Atributos: Cor, circunferência, material
# • Métodos: trocaCor e mostraCor

class Bola:
    
    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferencia = circunferência
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)
        # ou return self.cor