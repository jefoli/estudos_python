# 191. Problema dos parâmetros mutáveis em funções Python

# Risco: Toda vez que chamarmos a func passarmos uma lista sem parâmetro,
# O Python vai reutilizar a mesma lista ou qualquer param mutável!
def add_clients(name, bd_list=[]):
    bd_list.append(name)
    return bd_list

client_1 = add_clients('Luiz')
add_clients('Joana', client_1)
print(client_1)

client_2 = add_clients('Barney')
add_clients('Harry', client_2)
print(client_2)

# FORMA de evitar esse erro:

# Melhor forma -> NÃO usar os params mutáveis em params/valor padrão da função

# 2) ter uma lista fora da função:
list_1 = [] # essa lista que será usada!


# 3) inserir um none no param mutável!
# Toda vez que forma chamada, será criada uma nova lista!
def add_clientes_2(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

client_3 = add_clientes_2('Luiz', list_1)
add_clientes_2('Joana', client_3)
print(client_3)

client_4 = add_clientes_2('Eliseo')
add_clientes_2('Luiz', client_4)

# podemos editar essa lista:
add_clientes_2('Fernando', client_4)
client_4.append('Edu')
print(client_4)


#podemos criar lista separadas, pois uma não afeta outra!

client_5 = add_clientes_2('Juiz')
add_clientes_2('Vasconcelos', client_5)
print(client_5)


