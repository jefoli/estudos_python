# 122. (parte 2) Shallow Copy vs Deep Copy em dados mutáveis Python
'''
len - quantas chaves

keys - iterável com as chaves

values - iterável com os valores

items - iterável com chaves e valores

setdefault - adiciona valor se a chave não existe

copy - retorna uma cópia rasa (shallow copy) - faz uma cópia e todos items imutáveis para outro dict.
Obs: Se você alterar o valor mutável na cópia, ele vai alterar do dict origina também.
get - obtém uma chave

deepcopy (deep copy) - tem que importar um método (import copy) - Faz uma cópia dos valores mutáveis imutáveis!

pop - apaga um item cm a chave especificada (del)

popitem - apaga o último item adicionado

update - atualiza um dicionário com outro

'''

import copy

pessoa = {
    'nome': 'Marcos',
    'sobrenome': 'Steves',
    'idade': 40,
    'vl_mutavel': [0,4,47]
}

# shallow copy:
pessoa_2 = pessoa.copy()

print(pessoa_2)


# deep copy
pessoa_3 = copy.deepcopy(pessoa)

pessoa_3['vl_mutavel'][0] = 33965 # alterou o vl mutável sem alterar o dict original.

print(pessoa_3)

