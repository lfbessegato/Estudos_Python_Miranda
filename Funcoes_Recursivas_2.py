from typing import List
from collections import namedtuple

Caixa = namedtuple('Caixa', 'tem_chave')

def encontra_chave(caixas: List[Caixa], index: int = 0) -> Caixa:
    # Caso Base
    if len(caixas) <= index:
        return Caixa(False)

    caixa = caixas[index]
    print(f'Buscando chave na caixa de índice {index} -> {caixas}')

    # Caso Base
    if caixa.tem_chave:
        return caixa

    # Caso Recursivo
    index += 1
    return encontra_chave(caixas, index)


if __name__ == "__main__":
    caixas: List[Caixa] = [
        Caixa(False), Caixa(False), Caixa(False),
        Caixa(False), Caixa(False), Caixa(False),
        Caixa(False), Caixa(True), Caixa(False),
    ]

    print(encontra_chave(caixas))