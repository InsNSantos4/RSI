import math

class PizzaGrande():
    """ PizzaGrande encapsula uma pizza com 50cm de diãmetro, que tem um
    nome e uma lista de ingredientes como atributos"""
    diametro_cm=50

    """
    Inicializa um novo objeto PizzaGrande
    :param nome: nome da pizza
    :param pizzaingredients: lista de ingredientes da pizza (cada ingrediente é uma str)
    :returns nothing 
    """
    def __init__(self, nome, pizza_ingredients = ["tomate", "queijo mozarella"] ):
        self.nome = nome
        self.ingredients = pizza_ingredients
    
    """
    Retorna o nome da pizza em maiúsculas.
    """
    def get_upper(self):
        return self.nome.upper()
    
    """
    Calcula e devolve a área da pizza, em centímetros quadrados.
    """
    def pizza_area(self):
        return math.pi * ((self.diametro_cm/2)**2)

pizza_vegetariana = PizzaGrande("Vegetariana",["queijo", "pimentos","orégãos", "milho" ] )