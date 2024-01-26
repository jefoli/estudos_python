# 149-150 - try e except para tratar exceções:

"""
documentação oficial: https://docs.python.org/pt-br/3/library/exceptions.html

Zen of Python: Errors should never pass silently.

Exception - Classe superior que trata qualquer erro que ocorrer que não estamos tratando.

Obs: podemos tratar mais de um erro na mesma linha,
porém não é indicado já que prcisamos saber exatamente o erro que ocorreu.
No entanto, se desejar manter, podemos utilizar 'as'(alias) + var para ter a instância do erro.
"""

# Má prática deixar nos moldes abaixo, pois estamos silenciando um erro:
try:
    a = 18
    b = 0
    print('line 1')
    c = a / b
    print('line 2')
except:
    print('Realizou divisão por zero.')
    # dessa forma pode ter mais erros e não será visto
print('continue\n')

n1 = 10
n2 = 0

# forma correta - passar uma class de erro:
try:
    print('line 1')
    c = n1/n2
    print(c)

except ZeroDivisionError:
    print('Divisão por zero')
print()

try:
    print('line 1')
    c = n1/n3
    print(c)

except ZeroDivisionError:
    print('Divisão por zero')
except NameError:
    print('D não está definido')
print()


#tratando 2 erros na mesma linha:
try:
    num_1 = 20
    num_2 = 0
    print('Line 1'[1000])
    
    division = num_1 / num_2

except ZeroDivisionError:
    print('Divisão por zero')
except NameError:
    print('D não está definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('Erro Desconhecido')
print()


#tratando 2 erros na mesma linha:
#podemos usar 'as' error, para devolver exato erro:
try:
    num_1 = 20
    num_2 = 0
    print('Line 1'[1000])
    
    division = num_1 / num_2

except ZeroDivisionError:
    print('Divisão por zero')
except NameError:
    print('D não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Msg:', error)
    print('Msg:', error.__class__.__name__) # Nome do erro

except Exception:
    print('Erro Desconhecido')
print()