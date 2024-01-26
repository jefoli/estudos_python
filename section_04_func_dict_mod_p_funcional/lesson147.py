# 147. Introdução às Generator functions em Python
'''
yield (pausa função) -> toda função geradora utiliza a palavra yield para pausar.
'''

def generator(n=0):
    yield 1
    print('Continuando ...')
    yield 2
    print('Continuando novamente')
    yield 3
    print('Vou terminar')
    return 'Finalizado'

gen = generator(n=0) # temos que executar a função para funcionar

for n in gen:
    print(n)


def generator_2(num=0, maximum = 10):

    while True:
        yield num
        num += 1
        
        if num >= maximum:
            return
        

gen_2 = generator_2()

for i in gen_2:
    print(i)
print()

# exibir 100 num
gen_3 = generator_2(maximum=100)
for num in gen_3:
    print(num)