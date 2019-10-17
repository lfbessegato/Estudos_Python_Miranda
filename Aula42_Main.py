from Aula42_Agregação import CarrinhoDeCompra, Produto

carrinho = CarrinhoDeCompra()
print(carrinho)

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.lista_produto()

print('Compra *******')
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

print('******** Mostra')
carrinho.lista_produto()
print(carrinho.soma_total())
