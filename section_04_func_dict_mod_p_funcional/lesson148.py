# 148. yield from em generator functions
# Podemos dar continuidade a um generator usando outro generator com FROM
def gen1():
    yield 1
    yield 2
    yield 3
    print('Finish gen 1')

def gen2():
    if gen1 is not None:
        yield from gen1()
    yield 4
    yield 5
    yield 6
    print('Finish gen 2')

g = gen2()

for numero in g:
    print(numero)