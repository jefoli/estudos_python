# 176. map, partial, GeneratorType e esgotamento de Iterators
'''
map - faz o mapeamento dos dados. (é um iterator!)
    - 1 param: recebe uma func
    - 2 param: recebe um iterável

functools - ferramentas para funções
    - partial: New function with partial application of the given arguments and keywords.


GeneratorType - Checa se é uma instância de generator type

Obs: um iterator é esgotável, logo podemos converter antes

'''

from functools import partial 
from types import GeneratorType

#função map padrão:
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'nome':'produto 5', 'preco': 10.00},
    {'nome':'produto 1', 'preco': 22.32},
    {'nome':'produto 3', 'preco': 10.11},
    {'nome':'produto 2', 'preco': 105.87},
    {'nome':'produto 4', 'preco': 69.90},
]

def increase_percent(value, percent):
    return round(value * percent, 2)


# partial
inc_ten_percent = partial(increase_percent, percent = 1.1)


def change_product_price(product):
    return {**product, 'preco': inc_ten_percent(product['preco'])}




new_products_1 = [{**p, 'preco': inc_ten_percent(p['preco'])} for p in products]


# map tem as mesma função de new_products_1
new_products_2 = map(
    change_product_price, products
)

# podemos exibir o map com comprehension:
show_new_products_2 = [x for x in new_products_2]
print(products)
print(show_new_products_2)

# podemos exibir com list:
print(list(new_products_2))

#verifica se é um generator:
print(isinstance(new_products_2, GeneratorType))



# podemos usar map + lambda
# retorna um iterator
#para evitar que o iterator se esgote, converter para list:
print(list(map(lambda x: x * 3, [1,2,3,4,])))