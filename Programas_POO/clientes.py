class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

    # Getter para obter o valor do atributo nome
    def obter_nome(self):
        return self.nome

    # Getter para obter o valor do atributo endereco
    def obter_ender(self):
        return self.endereco
