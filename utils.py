def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
         texto = ' Bytes'
    elif tamanho < mega:
        tamanho /= kilo
        texto = ' KB'
    elif tamanho < giga:
        tamanho /= mega
        texto = ' MB'
    elif tamanho < tera:
        tamanho /= giga
        texto = ' GB'
    elif tamanho < peta:
        tamanho /= tera
        texto = ' TB'
    else:
        tamanho /= peta
        texto = ' PT'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')