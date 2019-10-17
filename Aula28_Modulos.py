# Módulos padrão do Python
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# veja todos os módulos padrão do python em:
# https://docs.python.org/3/py-modindex.html

# import sys
import random
from sys import platform as so
# ----------- Sample 1
# print(sys.platform)
print(so)
# ----------- Sample 2
for i in range(10):
    print(random.randint(1,10))

