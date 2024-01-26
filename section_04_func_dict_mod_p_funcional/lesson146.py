# 146. Generator expression, Iterables e Iterators em Python
'''
generator = são funções que sabem pausar em deteminada ocasião.
Todo gerenator é um iterator, porém o inverso não é verdade.

Para utilizarmos uma generaton expression temos usar ().
OBS(1): É muito similar a comprehension expression, porém usa () ao invés de []
OBS(2): Generator não tem tamanho e nem índice que uma lista tem.

Funcionamento da Generator Expression:

A generator expression não guarda todos os valores em memória, ela age como um loop que gera valores conforme necessário.

Ela "lembra" onde parou internamente e não precisa armazenar os valores gerados, diferente da lista!
'''
import sys

iterable = ['EU', 'Tenho', '__iter__']

lista = [n for n in range(1000)]
print(lista)

#cria um generator -> ()
generator = (n for n in range(10))
print(generator)
# para ver o primeiro valor, tem que dar um next:
print(next(generator))
print(generator.__next__())

# getsizeof -> retorna o tamanho da lista em bytes na memória:
print('Bytes list[]:', sys.getsizeof(lista))
print('Bytes generator():', sys.getsizeof(generator))
# por conta disso, podemos ver que a lista consome mais memória que generator, por armazenar todos valores na memória.