"""
public, pretected, private
Por convenção por utilizar _ ou __
__ O atributo não é para ser acessado
__ privado (_NOMEDACLASSE_nomedoatributo)
"""
print('Aula 40 - Encapsulamento')
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.apaga_cliente(2)
bd.lista_clientes()

bd.__dados = 'Outra coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados)