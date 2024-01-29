# 159. __init__.py é um arquivo de inicialização dos packages em Python
'''
Podemos colocar um arquivo de inicialização do package,
com a criação de um arquivo chamado __init__.py

Dessa forma, tudo que for importado dentro do package será executado

Qualquer coisa que for executado no __init__.py(pasta lesson153_modulo) ficará disponível no package

Podemos utilizar isso para "enganar o python", para fazer o package parecer um módulo
e ser possível importar objetos a partir dele
'''

import lesson155_package 

print(lesson155_package.dobrar_valor(3))

# TUDO QUE TIVER IMPORTADO NO __init__.py podemos utilizar aqui!
print(lesson155_package.somar(3,5))