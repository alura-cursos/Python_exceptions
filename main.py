from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


cliente = Cliente("John Doe", "123.456.789-00", "Desenvolvedor")
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)
cliente.idade = 20

print(cliente.idade)