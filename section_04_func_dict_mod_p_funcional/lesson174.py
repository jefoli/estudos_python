# 174. Combinations, Permutations e Product - Itertools (módulo)
'''
Combinations - Ordem não importa - iterável + tamanho do grupo

Permutação - Ordem importa

Produto - Ordem importa e repete valores únicos

retorna um iterator(usamos list para ver o resultado)

article: https://glenncallejafrendo.medium.com/products-permutations-combinations-combinations-with-replacement-in-python-2b113a6f942b

'''

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

persons = ['João', 'Joana', 'Luiz', 'Leticia',]

t_shirts = [['preta', 'branca'],
            ['p', 'm', 'g'],
            ['masculino', 'feminino', 'unisex'],
            ['dry fit', 'poliester']]

#faz combinações
print_iter(combinations(persons, 2)) 

#permutação
print_iter(permutations(persons, 2)) 


# produto cartesiano
print_iter(product(*t_shirts))