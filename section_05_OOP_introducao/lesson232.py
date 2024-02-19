# 233. Criando Exceptions em Python Orientado a Objetos (Exceções)
# 234. Levantando e tratando suas Exceptions (Exceções)
# 235. Notas das exceptions em Python 3.11+ (add_notes, __notes__)

'''
Para criar uma Exception em Python, basta herdar de alguma exceção da linguagem.

Recomendação: herdar de Exception
https://docs.python.org/3/library/exceptions.html

exceções - Levantando (raise) python  / Lançando(Throw) outras linguagens 

Relançando exceções

Por convenção, é necessário colocar a palavra 'Error' ao final.

conforme documentação, temos que herdar de Exception

. add_note() -> Podemos lançar uma nota de erro a partir do Python 3.11

'''

class MyError(Exception):
    ...

class OtherError(Exception):
    ...

def levantar():
    exception_ = MyError('a', 'b', 'c')
    
    # Podemos lançar nota de erros
    exception_.add_note ('Olha a nota 1')
    exception_.add_note('Revise add notes')
    
    raise exception_

try:
    # 1/0
    levantar()

except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)

    #relançando a exceção:
    exception_ = OtherError('Lançando outro erro!')

    # copiando mensagem das notas:
    exception_.add_note('Lancei nova nota de erro')
    exception_.__notes__ += error.__notes__.copy()

    raise exception_ from error