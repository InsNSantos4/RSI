import math

class PizzaMedia():
    """ PizzaMedia encapsula uma pizza com 30cm de diãmetro, que tem um
    nome e uma lista de ingredientes como atributos"""
    
    diametro_cm=30

    """
    Inicializa um novo objeto PizzaMedia
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
    
#help(PizzaMedia)

pizza_vegetariana = PizzaMedia("Vegetariana",["queijo", "pimentos","orégãos", "milho" ] )
print(f"Ingredientes desta Pizza {pizza_vegetariana.nome}: {pizza_vegetariana.ingredients}")