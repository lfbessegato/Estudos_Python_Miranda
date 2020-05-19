nomes_de_pessoas = ['Luiz', 'Maria', 'João']
nome_que_eu_quero = 'Luiz'

print('Luiz' in nomes_de_pessoas)
print(nomes_de_pessoas.index('Luiz'))

if nome_que_eu_quero in nomes_de_pessoas:
    index = nomes_de_pessoas.index(nome_que_eu_quero)
    print(f'{nome_que_eu_quero} está na lista {nomes_de_pessoas}')
    print(f'O índice de {nome_que_eu_quero} é {index}')
else:
    print(f'{nome_que_eu_quero} não existe em {nomes_de_pessoas}')