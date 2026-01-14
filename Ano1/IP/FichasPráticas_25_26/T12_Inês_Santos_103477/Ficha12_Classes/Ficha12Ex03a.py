# Ficha12 Ex3a

#3. Crie uma classe Pessoa que modele uma pessoa, contendo os seguintes atributes e métodos:
#• Atributos: nome, idade, peso e altura e linguas
# • Métodos: Envelhecer, engordar, emagrecer, crescer, nova_lingua
#• Nota: a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, a pessoa deve crescer 0,5 cm."""

class Pessoa:
    '''Estaclasse modela uma pessoa'''

    def __init__ (self,nome='',idade=0,peso=0.0,altura=0.0,linguas=[]):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.linguas = linguas

    def envelhecer(self,anos):
        if self.idade >= 21:
            self.idade += anos
        elif self.idade + anos < 21:
            self.idade += anos
            self.altura += anos*0.05
        else:
            self.altura += (20 - self.idade) *0.005
            self.idade += anos

    def engordar(self,quilos):
        self.peso += quilos

    def emagrecer(self,quilos):
        self.peso -= quilos

    def crescer(self,metros):
        self.altura += metros

    def nova_lingua(self,ling):
        self.linguas.append(ling)



pop=Pessoa('Jorge',15,62,1.65,['Frances','Ingles','Alemao'])
pop.crescer(0.05)
vm=Pessoa()
print('Linguas:', pop.linguas)
print('Altura:', pop.altura)

pop.envelhecer(7)
pop.engordar(10)
print('Idade:', pop.idade)
print('Altura:', pop.altura)
print('Peso:', pop.peso)

print('Linguas:', pop.linguas)
pop.nova_lingua('Portugues')
print('Linguas:', pop.linguas)