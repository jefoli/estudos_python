# 178. reduce - faz a redução de um iterável em um valor
'''
reduce: tem a função de reduzir um iteravel em um único valor

Obs: É necessário importar de 'functools' para utilizar.

Função reduce precisa de um contador para não ter algum tipo de problema!

Sempre vai retornar um acumulador e o produto que está iterando!

'''
from functools import reduce

products = [
    {'nome':'produto 5', 'preco': 10},
    {'nome':'produto 1', 'preco': 22},
    {'nome':'produto 3', 'preco': 2},
    {'nome':'produto 2', 'preco': 6},
    {'nome':'produto 4', 'preco': 4},
]

total = 0
for p in products:
    total += p['preco']
print(total, sep='\n')


# com a func sum
print(sum([p['preco'] for p in products]))


# reduce:

# tem que criar uma função do reduce
# recebe 2 params: 1(acumulador), 2 produto
# Sempre vai retornar um acumulador e o produto que está iterando!
def func_reduce(acumulator, product):
    print(acumulator)
    print('product: ', product)
    print()
    return acumulator + product['preco'] # o valor que retornar vai ser o acumulator!

# precisa passar um valor inicial para evitar eventual erro. no exp '0'
total_reduce = reduce(func_reduce, products, 0)
print('Total Reduce:', total_reduce)

#OBS: podemos resolver com uma lambda sem a necessidade de escrever a lógica acima
total_reduce_with_lambda = reduce(lambda ac, p : ac + p['preco'], products, 0)
print('Total :', total_reduce_with_lambda)