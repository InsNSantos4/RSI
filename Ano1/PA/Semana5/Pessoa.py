class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    #Getter 
    def getNome (self):
        return self.nome + " " + self.sobrenome
    
    #Override de __str()__
    def __str__(self):
        return self.nome + " " + self.sobrenome