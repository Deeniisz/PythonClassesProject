class Produto:
    def __init__(self, ID, nome, preco, entrada, saida):
        self.ID = ID
        self.nome = nome
        self.preco = preco
        self.entrada = entrada
        self.saida = saida

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setNome(self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome

    def setPreco(self, preco):
        self.preco = preco

    def getPreco (self):
        return self.preco

    def setEntrada(self, entrada):
        self.entrada = entrada

    def getEntrada (self):
        return self.entrada

    def setSaida(self, saida):
        self.saida = saida

    def getSaida (self):
        return self.saida