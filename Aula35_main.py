from Aula35_OO_Pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Joao', 32)

# Chamando os métodos
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('banana')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('laranja')
p1.falar('JAVA')
p1.parar_falar()
p1.comer('Laranja')
p1.parar_comer()
print()

# Chamando os métodos para mais de uma pessoa
print('** Segunda Etapa **')
p1.falar('POO')
p2.comer('Sorvete')
p1.comer('churrasco')
print()


# Chamando os métodos para mais de uma pessoa
print('** Terceira Etapa **')
print(p1.ano_atual)
print(p2.ano_atual)
print()
print(f'O ano de nascimento de {p1.nome} é {p1.get_ano_nascimento()}')
print(f'O ano de Nascimento de {p2.nome} é {p2.get_ano_nascimento()}')
