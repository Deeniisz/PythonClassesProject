class Cliente:
    def __init__(self, ID, nome, telefone, endereco, cidade, estado, nasc):
        self.ID = ID
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.nasc = nasc

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def setNome(self, nome):
        self.nome = nome

    def getNome (self):
        return self.nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone (self):
        return self.telefone

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco (self):
        return self.endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade (self):
        return self.cidade

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setNasc(self, nasc):
        self.nasc = nasc

    def getNasc (self):
        return self.nasc