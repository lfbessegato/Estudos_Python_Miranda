import sys
import time

def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r

# Iteravel
lista = [0,1,2,3,4,5,6]
# Iterador
for v in lista:
    print(v)
print(hasattr(lista, '__iter__'))

# Iterador um valor de cada vez
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# Geradores = consumos
g = gera()

for v in g:
    print(v)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

l1 = [x for x in range(1000)]
print(type(l1))
l2=(x for x in range(1000))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
