class Loja:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, nome, preco, quantidade):
        self.produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}

    def atualizar_preco(self, codigo, novo_preco):
        if codigo in self.produtos:
            self.produtos[codigo]["preco"] = novo_preco

    def atualizar_quantidade(self, codigo, nova_quantidade):
        if codigo in self.produtos:
            self.produtos[codigo]["quantidade"] = nova_quantidade

    def remover_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo] # ou self.produtos.pop(codigo)

    def visualizar_produtos(self):
        for codigo, info in self.produtos.items():
            print(f"Código: {codigo}, Nome: {info['nome']}, Preço: {info['preco']}, Quantidade: {info['quantidade']}")

# Exemplo de teste
loja = Loja()
loja.adicionar_produto("001", "Caneta", 1.5, 100)
loja.adicionar_produto("002", "Caderno", 3.5, 50)
loja.atualizar_preco("001", 2.0)
loja.atualizar_quantidade("002", 60)
loja.remover_produto("001")
loja.visualizar_produtos()
