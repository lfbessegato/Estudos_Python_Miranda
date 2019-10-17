# https://docs.python.org/3/library/functions.html#open

import json

try:
    file = open('D:/Treinamento/Python/Miranda/abc.txt', 'w+')
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    # para voltar para o inicio do arquivo texto
    file.seek(0, 0)
    print('Lendo Linhas: ')
    print(file.read())
    print('###############')
    file.seek(0, 0)
    # ler linha por linha
    print(file.readline(), end='')
    print(file.readline(), end='')
    print('###############')

    file.seek(0, 0)
    print(file.readlines())
    print('###############')

    with open('D:/Treinamento/Python/Miranda/abc1.txt', 'w+') as file:
        file.write('Teste1\n')
        file.write('Teste2\n')
        file.write('Teste3\n')

        file.seek(0)
        print(file.read())
    print('##############################')
    with open('D:/Treinamento/Python/Miranda/abc1.txt', 'a+') as file:
            file.write('Teste4\n')
            file.write('Teste5\n')
            file.write('Teste6\n')

            file.seek(0)
            print(file.read())
finally:
    file.close()

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Maria',
        'idade': 30,
    },
}

print(d1)

d1_json = json.dumps(d1, indent=True)
with open('D:/treinamento/python/miranda/abc.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)