# 123. (Parte 3) Métodos úteis nos dicionários Python (dict)
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

get - obtém uma chave (podemos passar um valor padrão, caso não exista a key)

pop - apaga um item com a chave especificada (del)

popitem - apaga o último item adicionado
    Obs: não precisa passar nada dentro de parenteses, pois retorna a última chave

update - atualiza um dicionário com outro
    Obs1: O update pode atualizar uma chave existente ou criar uma nova!
    Obs2: Podemos passar argumentos nomeados
    Obs: Podemos escrever com tuplas também
'''

p1 = {
    'nome': 'Felipe',
    'sobrenome': 'Steves',
    'idade': 70,
}

print(p1.get('nome'))
print(p1.get('casa')) # não existe
print(p1.get('casa', 'Não existe!')) #get c/ valor padrão

# pop:
name = p1.pop('nome')
print(name)
print(p1)

# popitem:
eliminar_idade = p1.popitem()
print(eliminar_idade)
print(p1)

#Update - atualiza o dict:
p1.update({'nome': 'Cadu', 'telefone': '2222-2222'})
print(p1)

#update c/ argumentos nomeados
p1.update(rua = 'Avenida padrão', cep = '11111-222')
print(p1)


#upadate c/ tuplas
tupla = (('Bairro', 'Vila Brasil'), ('número', 50))
p1.update(tupla)
print(p1)

#update c/ listas
lista = [['estado civil', 'solteiro'], ['dependente', 'não']]
p1.update(lista)
print(p1)