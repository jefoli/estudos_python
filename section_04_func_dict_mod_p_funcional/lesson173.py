# 173. count é um iterador sem fim (itertools)
'''
- count() está no módulo 'itertools

- count é um contador infinito!

- podemos passar o inicio, step e keywords: 
    exp: 
        - count(initial, step)
        - count(step=8, start=8)

count() != range(), pois podemos passar um end para o range()
'''

from itertools import count

#c1 = count(8, 8)
c1 = count(start=2, step=2)

# verificar se possui atributos especiais:
print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))

# count
for i in c1:
    if i > 100:
        break
    print(i)