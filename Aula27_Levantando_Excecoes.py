# https://docs.python.org/3/library/exceptions.html

def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise

def divide1(n1,n2):
    if n2 == 0:
        raise ValueError ("n2 não pode ser 0.")
    return n1 / n2
print('-=' * 30)
try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)

print('-=' * 30)
try:
    print(divide1(n1=2, n2=0))
except ValueError as error:
    print('Você está tentando dividir por zero.')
    print('Log: ', error)