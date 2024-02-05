#169-172. Exercício - Unir listas
'''
Objetivo = Treinar lógica de programação + conhecer a class zip()

- Criar uma função zipper que una dias listas na ordem
- Use todos os valores da menor lista
Exp:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', SP', 'MG', 'RJ']
OUTPUT: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

zip() - utiliza a MENOR lista e faz a concatenação das listas e retorna um iterator!
    - zip só une as listas até o tamanho da menor lista!
    - Para vermos os valores,podemos usar list() ou fazer um for in. 

zip_longest - utiliza MAIOR lista. (TEM QUE IMPORTAR)
    - from itertools import zip_longest
    
    - Podemos passar um (fillvalue ='Sem cidade') quando não houver infos
    conseguimos capturar os valores restantes da lista maior, sem obter um erro em nosso programa.

'''
from itertools import zip_longest

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
state = ['BA', 'SP', 'MG', 'RJ']

def zipped(*city):
    qtd_cities = len(city[0])
    
    new_list = []
    
    cidade = [x for x in city[0]]    
    estado = [y for y in city[1]]
    
    for i in range(qtd_cities):
        new_list.append(tuple([cidade[i], estado[i]]))
    
    return new_list

concat_list = zipped(cities, state)

print(concat_list)


# sugestão de resposta:
def zipper(list1, list2):
    max_interval = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(max_interval)]
print(zipper(cities, state))


# class zip
class_zip = zip(cities, state)
print(class_zip)
print(list(class_zip))

# func zip_longest
zipper_longest = zip_longest(cities, state, fillvalue ='Sem cidade')
print(list(zipper_longest))
