# 120. Manipulando chaves e valores em dicionários em Python

pessoa = {}

# criar chave:
pessoa['nome'] = 'Marcos Silva'

chave_dinamica = 'sobrenome'

pessoa[chave_dinamica] = 'Costa'

print(pessoa)

#acessar chave
print(pessoa['nome'])


# apagar chave:
pessoa['telefone'] = '1111-1111'
print(pessoa)

del pessoa['telefone']
print(pessoa)

# acessar chave que não existe p/ não causar erro:
# utilizar o método .get() do dicionário:

# OBS: O padrão é retornar None se a chave não existir:
# print(pessoa.get('Telefone'))

if pessoa.get('sobrenome') is None:
    print('chave não existe!')
else:
    print(pessoa['sobrenome'])