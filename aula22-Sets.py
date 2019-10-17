# add (Adiciona), update(Atualiza), clear, discard
# union | (une)
# Intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5,6}
for v in s1:
    print(v)

# Inicializa o set como vazio
s2 = set()

# Adiciona valores em sets
s2.add(1)
s2.add(2)

print (s2)

# Remove um elemento
s2.discard(2)
print(s2)

# Update - intera
s2.update('Python')
print(s2)

# Union
st1 = {1,2,3,4,5}
st2 = {1,2,3,4,5,6}
st3 = st1 | st2
print(st3)

# Intersection
st4 = st1 & st2
print(st4)

# Difirrence
st5 = st2 - st1
print(st5)