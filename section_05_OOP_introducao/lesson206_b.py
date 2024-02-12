# 206. Exercício - Salve sua classe em JSON
'''
Salvar os dados da sua classe em JSON
e depois criar novamente as instâncias da classe com os dados salvos.
Salvar em um arquivo separado
'''
import json

from lesson206_a import FILE_PATH, Person

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    pessoas = json.load(file)

    for pessoa in pessoas:
        p = Person(**pessoa)
        print(p.nome, p.idade)
