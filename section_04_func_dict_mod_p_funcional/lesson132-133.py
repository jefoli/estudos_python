# 132-133. Introdução à função lambda + list.sort e sorted
"""
Uma função lambda em Python é uma função anônima que pode ser definida sem um nome. 

Ela é uma função pequena e simples que pode ser criada em uma única linha de código. 

Obs:
    sort() - Ordena uma lista
    sorted() - Retorna uma nova cópia da lista (shallow copy)
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Daniel', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    # print(item)
    return item['nome']

lista.sort(key=ordena)
print(lista)
print()

# mesma função, porém em lambda:
lista.sort(key=lambda item: item['nome'])
print(lista)
print()


def exibir(lista):
    for item in lista:
        print(item)
    print()

#sorted(): retorna uma nova cópia da lista
l1 = sorted(lista, key=lambda item: item['sobrenome'])
l2 = sorted(lista, key=lambda item: item['nome'])

exibir(l1)
exibir(l2)