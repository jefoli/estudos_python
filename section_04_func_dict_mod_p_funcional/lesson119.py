# 119. Introdução ao tipo de dados dict - Dicionários em Python
'''
Dicionários são estruturas de dados do tipo par de "chave" e "valor" (key/word) e são mutáveis.

Chaves podem ser consideradas como o "índice".

As chaves podem sem criadas como qualquer tipo imutável (str, int, float, bool, tuple, etc)

O valor pode ser qualquer tipo, podendo incluir outro dicionário dentro.

formas de criar um dicionário:
    
    -> Usar chaves - {}
        exp: dicionario_1 = {}
    
    -> (menos utilizado) - Classe dict - dict() - 
        exp: dic_2 = dict(nome = 'Fernando')

'''

pessoa = { 
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'Endereços': [
        {'rua':'Avenida Brasil', 'numero': 123},
        {'rua':'Avenida Juscelino', 'numero': 500},
    ]
}

print(pessoa)
print()
print(pessoa['nome'])
print()
print(pessoa['Endereços'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])