class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} Falando ...')

"""
As classes Cliente e Aluno, herdam da classe Pessoa
"""
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} Comprando ...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} Estudando ...')