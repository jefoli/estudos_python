# 135. Empacotamento e desempacotamento de dicionários + *args e **kwargs
'''
*args - argumentos não nomeados
**kwargs - argumentos nomeados
    Obs: sempre usar 2 asteriscos
'''

#desempacotamento:
a, b = 1, 2

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

# pega as chaves
a, b = pessoa
print(a, b)

# pega os valores
a, b = pessoa.values()
print(a, b)

# retorna uma tupla chave e valor
a, b = pessoa.items()
print(a, b)

# desempacotar internamente:
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)


pessoa2 = {
    'nome': 'Carla',
    'sobrenome': 'Medeiros'
}

dados_pessoais = {
    'idade': 16,
    'altura': 1.6,
}

#desempacotamento de dict:
pessoa_completa = {**pessoa2, **dados_pessoais}
print(pessoa_completa)


#kwargs - empacotando argumentos
def mostrar_argumentos_nomeados(*args, **kwargs):

    print('Args não nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados(1,20, nome='Joana', idade=20)


# desempacotar dict
mostrar_argumentos_nomeados(**pessoa_completa)