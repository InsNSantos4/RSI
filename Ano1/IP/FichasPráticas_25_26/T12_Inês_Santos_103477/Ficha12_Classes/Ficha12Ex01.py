# Ficha 12 Ex01

# Crie uma Classe Bola que modele uma bola.


class Bola:
    '''Classe Bola que modele uma bola. A classe deverá conter os seguintes atributos e métodos:
        Atributos: Cor, Circunferência, Material
         Métodos: trocaCor e mostraCor'''

    def __init__(self, Cor, Circunferencia, Material):
        self.Cor = Cor
        self.Circunferencia = Circunferencia
        self.Material = Material

    def __str__(self):
        return f'Cor: {self.Cor} \nRaio: {self.Circunferencia} \nMaterial: {self.Material}'

    def trocaCor(self,novaCor):
        self.Cor = novaCor

    def mostraCor(self):
        print(f'Cor: {self.Cor}')
        return self.Cor


bfut = Bola('branca',20,'couro')


bfut.mostraCor()
bfut.trocaCor('Azul')
bfut.mostraCor()
bfut.trocaCor('verde')
bfut.mostraCor()
print(bfut)
band = Bola('verde',30,'plastico')
band.mostraCor()
band.trocaCor('Azul')
band.mostraCor()
band.trocaCor("Castanha")
band.mostraCor()
print(band)
print(f'A bola de Andebol é {band.mostraCor()}')


print()

exit()
########################################3
def __str__(self):
    return f'Cor: {self.Cor} \nRaio: {self.Circunferencia} \nMaterial: {self.Material}'


print(bfut)