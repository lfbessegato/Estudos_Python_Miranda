lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x, y in lista}
print(d1)

#----------
d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

#---------
d3 = {x for x in range(5)}
print(d3, type(d3))

#---------
d4 = {f'chave_{x}': x**2 for x in range(5)}
print(d4,type(d4))