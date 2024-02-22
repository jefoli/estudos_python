# 250-251. dir e help + DocStrings (Documentação)

"""Docstring de uma linha"""

""" Docstring de varias linha
dir -> mostra tudo que tem dentro de um módulo na forma de uma lista de str.

help() -> Solicitamos ajuda ao py para vermos o que tem dentro do módulo

docstrings -> variáveis c/ 3 aspas simples ou duplas e servem como documentação 
do módulo.

Recomendação PEP8 -> Máximo de 79 caracteres em uma linha.
Dica p/ VSCODE: em setings, inserir: "editor.rulers": [80], para criar uma
linha de marcação visando não ultrapassar a qtd. caracteres

Recomendação PEP8 -> criar docstrings com aspas duplas 
"""

import lesson246

name = 'name dentro do mod.'

print(dir())
#print(dir(name))
# print(dir(lesson246.Dividir.__name__))
help()
help(lesson246)