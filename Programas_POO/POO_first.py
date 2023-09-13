# exemplo 1
class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

    def imprimir(self):
        print(f'Nome: {self.nome}, Endereço: {self.ender}')




class Profissao(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def imprimir(self):
        super().imprimir()
        print("\t e trabalha como ", self.profissao)


p = Profissao("Ana", 25, "Balconista")
p.imprimir()

pessoa1 = Pessoa("Maria", "rua 01234")
pessoa2 = Pessoa("João", "rua 45678")

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')

print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')
