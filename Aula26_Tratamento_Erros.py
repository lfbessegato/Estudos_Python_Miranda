#------------- Sample 1
print('Sample 1' )
try:
    print(a)
except NameError as erro:
    print('Erro: ', erro)
except Exception as erro:
    print ('Erro Inesperado: ', erro)
print('Fim - Sample 1')
print ('-=' * 30)
#------------ Sample 2
print('Sample 2')
try:
    a=[]
    print(a[1])
except NameError as erro:
    print('Erro: ', erro)
except Exception as erro:
    print ('Erro Inesperado: ', erro)
print('Fim - Sample 2')
print ('-=' * 30)
#---------- Sample 3
print('Sample 3')
try:
    a={}
    print(a[1])
except NameError as erro:
    print('Erro: ', erro)

except IndexError as erro:
    print('Erro de índice.')

except Exception as erro:
    print ('Erro Inesperado: ', erro)
print('Fim - Sample 3')
print ('-=' * 30)
#--------------- Sample 4
print('Sample 4')
try:
    a = {}

except NameError as erro:
    print('Erro: ', erro)

except IndexError as erro:
    print('Erro de índice.')

except Exception as erro:
    print('Erro Inesperado: ', erro)
else:
    print('Seu código foi executado com sucesso.')
    print(a)
print('Fim - Sample 4')
print('-=' * 30)
#--------------- Sample 5
print ('Sample 5')
try:
    a = {}
except NameError as erro:
    print('Erro: ', erro)

except IndexError as erro:
    print('Erro de índice.')

except Exception as erro:
    print('Erro Inesperado: ', erro)
else:
    print('Seu código foi executado com sucesso.')
    print(a)
finally:
    print('Finalmente')
print('Fim - Sample 5')
print('-=' * 30)
