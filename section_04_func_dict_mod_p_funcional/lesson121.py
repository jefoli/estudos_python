# 121. (Parte 1) Métodos úteis nos dicionários Python (dict)
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
pessoa = {
    'nome': 'Marcos',
    'sobrenome': 'Steves',
    #'idade': 40,
}

# len:
print(len(pessoa))

# keys:
print(tuple(pessoa.keys()))

for chave in pessoa.keys():
    print(chave)

# values - só valores:
print(list(pessoa.values()))

for valor in pessoa.values():
    print(valor)

#items:
print(list(pessoa.items()))

for key, value in pessoa.items():
    print(key, value)

#setdefault:
pessoa.setdefault('idade', None)
print(pessoa['idade'])
    

