# 157. Introdução aos packages (pacotes) em Python
'''
package - É uma pasta que possui módulos python.
    - a pasta não pode ter espaço, letra maíuscula, etc...

A melhor forma de organizar um arquivo, é criar um arquivo __main__ (arquivo de entrada) na raiz e 
depois os packages
'''

#from sys import path
#print(path, sep='\n')

# importa o package, porém não tem muita funcionalidade
import lesson155_package


# 1) forma(+prática): importar o package com a função
from lesson155_package.modulo import somar

# 2) forma:
from lesson155_package import modulo

# 3) forma(+verboso): tem que usar todo nome como namespace
import lesson155_package.modulo

print(somar(3,5)) # saída -> 1) forma
print(modulo.somar(4,1)) # saída -> 2) forma
print(lesson155_package.modulo.somar(5,6)) # saída -> 3) forma

'''
má pratica - para evitar utilização de alguma var que não desejamos
criamos no módulo __all__, pois quando fizermos a forma abaixo, só o que estiver
disponível dentro de __all__ que será retornado para uso.
'''
from lesson155_package.modulo import *
print(variavel) 


