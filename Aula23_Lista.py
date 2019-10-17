l1 = [1,2,3,4,5,6]
l2 = [variavel for variavel in l1]
print(l2)

#------
ex2 = [v * 2 for v in l1]
print(ex2)

#-------
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)

#--------
l3 =  ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a','@') for v in l3]
print(ex4)

#--------
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(x, y) for x, y in tupla]
print(ex5)

#-------
l4 = list(range(100))
ex6 = [v for v in l4 if v % 2 == 0 if v % 8 == 0]
print(ex6)
ex7 = [v if v % 3 == 0 else 'Não é' for v in l4]
print(ex7)