# 82. Tipo list - Introdução às listas mutáveis em Python
# 83. Concatenando e estendendo listas em Python
"""
Tipo list - É Mútavel

Suporta vários valores de qualquer tipo.

Metódos úteis:
    -> (insert) - adiciona elementos em qualquer local da lista.
        
        Obs_1: O método insert recebe dois argumentos:
            - primeiro argumento - Qual índice que iremos manipular
            - segunto argumento - qual valor queremos inserir.
            - .insert(indice, valor)
        
        Obs_2: Se passarmos um índice maior que o existente, ele vai inserir no 
        último independente de existir ou não tal índice
    
    -> (append) - adiciona objetos ao final da lista.
        Obs_3: Só é possível passar um argumento por append.

    -> (pop) - remove o último elemento da lista.
        Obs_4: toda vez que removermos um elemento da lista, esse valor é retornado.
    
    -> (del) - Deleta um índice.
    
    -> (clear) - limpa a lista.
    
    -> (extend) - extende uma lista.
        Obs_5: Não retorna valor, pois estende diretemante o valor a lista em que desejamos. 
        Por conta disso, se criarmos uma nova var e extende-lá, seu retorno será NONE

    -> (+) - Através do polimorfismo, podemos fazer o sinal de (+) se comportar de 
    outra maneira de modo a concatenar duas listas.
    
    - CRUD (Create, Read, Update, Delete) = list[i]

Obs_6: Quando deletarmos algum valor da lista, automaticamente será reorganizado os índices.

Obs_7: Em listas muitos grandes, merece maior atenção por conta da alteração dos 
índices em caso de CRUD.
"""

nova_lista = [20, 40, 66, 808]
print(nova_lista)

nova_lista.clear()
print(nova_lista)

# inserir valores utilizando o método insert:
nova_lista_2 = ['a', 230, 10]
print(nova_lista_2)

# var.insert(indice, valor)
nova_lista_2.insert(0, 'new_value')

print(nova_lista_2)

# Obs_2
nova_lista_2.insert(3000, 'adicionei')
print(nova_lista_2)
print(nova_lista_2[4]) # adicionou no índice 4 e não no 3000.


# Métodos para juntar listas:
lista_a = [1,2,3]
lista_b = [4,5,6]

# 1 forma - utilizando (+)
lista_c = lista_a + lista_b
print(lista_c)

# 2 forma - método extend:
lista_d = lista_a.extend(lista_b) # não retorna valor, pois estendeu os valores da lista_b na lista_a:
print('lista_a:', lista_a)

print(lista_d) # Quando colocarmos em uma nova var, seu retorno é NONE