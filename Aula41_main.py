print('Aula 41 - Associações')
from Aula41_POO_Associacoes import Escritor
from Aula41_POO_Associacoes import Caneta
from Aula41_POO_Associacoes import MaquinaDeEscrever

escritor = Escritor('Joazinho')
print(escritor.nome)

caneta = Caneta('BIC')
print(caneta.marca)

maquina = MaquinaDeEscrever()

print('---------------')
maquina.escrever()

print('-------------')
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

print('-------------')
escritor.ferramenta = maquina
escritor.ferramenta.escrever()