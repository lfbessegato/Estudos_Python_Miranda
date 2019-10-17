# import vendas.calcula_preco
from vendas.calcula_preco import aumento, reducao
from vendas.formata import preco as formatado

preco = 50.00
# vlr_aumento = vendas.calcula_preco.aumento(preco, 10)
vlr_aumento = aumento(preco, 15, formata=True)
print(vlr_aumento)

vlr_reducao = reducao(preco, 10,formata=True)
print(vlr_reducao)

print(formatado.real(50.96))