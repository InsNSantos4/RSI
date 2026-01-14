# Crie uma classe ContaCorrente para implementar uma conta corrente. A classe deve
# possuir os seguintes atributos e métodos:
# • Atributos: número da conta, nome do correntista e saldo.
# • Métodos: alterarNome, depósito e levantar;
# • No construtor poderá adicionar o atributo “saldo” com valor default zero.

class ContaCorrente:
    
    def __init__(self, account_number, correntista_name, amount = 0):
        self.num_conta = account_number
        self.nome_correntista = correntista_name
        self.saldo = amount
    
    def alterarNome(self, new_name):
        self.nome_correntista = new_name
    
    def deposito(self, add_amount):
        if add_amount > 0:
            self.saldo += add_amount
        else:
            print("Erro: O depósito deve ser um valor positivo.")
    
    def levantar(self, retrieve_amount):
        if retrieve_amount <= self.saldo and retrieve_amount >= 0:
            self.saldo -= retrieve_amount
        else:
            print("Erro: Não pode levantar mais do que o saldo que possui.")