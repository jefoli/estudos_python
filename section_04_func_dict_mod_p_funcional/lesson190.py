# 190. Salvando dados Python em JSON com módulo json
'''
Um arquivo JSON é um formato de texto que é usado para representar e trocar dados estruturados entre sistemas.

JSON significa JavaScript Object Notation, pois é baseado em um subconjunto da linguagem JavaScript. 

Um arquivo JSON contém apenas texto e usa a extensão .json. 
Ele é composto por uma coleção de pares nome/valor ou uma lista ordenada de valores, 
que podem ser strings, números, booleanos, arrays, objetos ou nulos.

Tem que colocar aspas duplas no arq JSON "".

- Muito utilizado para receber respostas!

dump = despejar

dump() = json.dump() converte o objeto Python em uma string JSON e escrever em um arquivo.

indent(dentro de dump) = '' - deixa o dicionário formatado

json.load(_arquivo_) -> carrega o arquivo
'''

# É necessário importar JSON e os(p/criar o path)
import json
import os

pessoa = {
    'nome': 'Luiz Fernando',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev' : True,
    'nada': None,
}

# colocar a extensão .json
# para windows -> colocar encoding='utf-8'
with open('lesson190.json', 'w', encoding='utf-8') as file:
    # faz um dump no arquivo:
    # ensure_ascii = False (coloca os acentos no json, etc)
    json.dump(pessoa, file, indent=4)



# Converter/retornar o json no programa:
with open('lesson190.json', 'r', encoding='utf-8') as file:
    #carrega o arquivo:
    pessoa = json.load(file) # retorna uma dict
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome']) # info está vindo de fora!
