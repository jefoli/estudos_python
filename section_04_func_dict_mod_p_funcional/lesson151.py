# 151. try, except, else e finally + Built-in Exceptions
'''
documentação oficial: https://docs.python.org/pt-br/3/library/exceptions.html

finally -> bloco que sempre será executado no try-except

'''
#podemos ter try/finally ou try/except/finally
try:
    print('Abrir arquivo')
finally:
    print('Fechar arquivo')

try:
    8/0
except ZeroDivisionError:
    print('erro: Divisão por zero!')
finally:
    print('Fechar arquivo')
print()

# podemos usar else:
try:
    8/1
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
    print('erro: Divisão por zero!')
else:
    print('Else: Não deu erro!')
finally:
    print('Finally: Fechar arquivo!')
print()