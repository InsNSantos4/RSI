# Crie uma Classe Quadrado que modele um quadrado, contendo os seguintes atributes e
# métodos:
# • Atributos: Tamanho do lado
# • Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

import math

class Quadrado:
    
    def __init__(self, side_size):
        self.tamanho_do_lado = side_size
    
    def mudarValorLado(self, novo_lado):
        self.tamanho_do_lado = novo_lado
    
    def mostrarLado(self):
        return self.tamanho_do_lado
    
    def calcularArea(self):
        #return self.tamanho_do_lado ** 2
        # OU
        return math.pow(self.tamanho_do_lado, 2)