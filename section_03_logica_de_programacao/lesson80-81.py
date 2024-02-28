# 80-81. Tipo list - Introdução às listas mutáveis em Python
# 81. Alterando uma lista com índices, del, append e pop (Tipo list)
"""
Tipo list - É Mútavel

Suporta vários valores de qualquer tipo.

Metódos úteis:
    - insert (inserir valores)
    - append (adiciona objetos ao final da lista)
        Obs_1: Só é possível passar um argumento por append.
    - pop (remove o último elemento da lista)
        Obs_2: toda vez que removermos um elemento da lista, esse valor é retornado.
    - del - Deleta um índice
    - clear
    - extend
        Obs_3: o método extend é usado para adicionar elementos de uma estrutura 
        iterável (como uma lista, tupla ou dict(insere a chave do dict)) ao final de outra lista.
    - CRUD (Create, Read, Update, Delete) = list[i]

Obs_4: Quando deletarmos algum valor da lista, automaticamente será reorganizado os índices.

Obs_5: Em listas muitos grandes, merece maior atenção por conta da alteração dos índices em caso de CRUD.

append vs extend:
O método append adiciona um único elemento ao final da lista.
O método extend é mais poderoso e pode adicionar múltiplos elementos de uma vez.

"""

string = 'ABCD'

# formas de criar uma lista:

# 1 forma:
lista_1 = list()

# 2 forma (mais comum):
lista_2 = [] # == '' (lista vazia)

print(lista_2, type(lista_2))

# podemos inserir vários types dentro da lista
lista_3 = [123, True, 'Carlota', 1.2, []]
print(lista_3)

# Podemos acessar os índices das listas
print(lista_3[2], type(lista_3[2]))

# Podemos alterar os valores da lista:
lista_3[-2] = 'Maria'
print(lista_3)


lista_4 = [10,20,30,40]

del lista_4[2] 

print(lista_4) # deletou o valor - 30

print(lista_4[2]) # atualizou o índice da lista.

# adicionar objetos ao final da lista:
lista_4.append('novo_texto')
print(lista_4)

# remover o último elemento da lista:
lista_4.pop()
print(lista_4)

valor_retornado = lista_4.pop()
print(f'{lista_4}, Valor removido da lista e retornado: {valor_retornado}')