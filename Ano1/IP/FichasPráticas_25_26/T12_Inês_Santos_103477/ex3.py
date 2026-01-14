# Crie uma classe Pessoa que modele uma pessoa, contendo os seguintes atributes e
# métodos:
# • Atributos: nome, idade, peso e altura
# • Métodos: Envelhecer, engordar, emagrecer, crescer.
# • Nota: a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, a
# pessoa deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, name, age, weight, height):
        self.nome = name
        self.idade = age
        self.peso = weight
        self.altura = height
    
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0,5
    
    def engordar(self, peso_mais):
        self.peso += peso_mais
    
    def emagrecer(self, peso_menos):
        self.peso -= peso_menos
    
    def crescer(self, altura_mais):
        self.altura += altura_mais