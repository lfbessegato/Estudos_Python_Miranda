from Aula44_Heranca import *
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()
print()

a1 = Aluno('Maria', 54)
print(a1.nome)
a1.falar()
a1.estudar()
print()

p1 = Pessoa('João', 43)
p1.falar()