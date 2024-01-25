#141. Dictionary Comprehension e Set Comprehension
# troca [] por {} + utiliza chave e valor
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}


dc_1 = {
    chave: valor for chave, valor in produto.items()
}

print(dc_1)


dc_2 = {
    chave: valor.upper() if isinstance(valor, str) else valor 
    for chave, valor in produto.items()
}

print(dc_2)



#novo dicionário a partir de uma lista:

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc_3 = {
    chave: valor for chave, valor in lista 
}
print(dc_3)

# tem a mesma função acima, porém reduzida
var_exp = dict(lista)
print(var_exp)


# Set Comprehension

s1 = {i for i in range(10)}
print(s1)