from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, num):
        super().__init__(nome, sobrenome)
        self.numMecanografico = num

    # getter
    def getAluno(self):
        return self.getNome() + ", " + str(self.numMecanografico)

    def __str__(self):
        return super().__str__() + ", " + str(self.numMecanografico)


print(Aluno("João", "Silva", 1234))