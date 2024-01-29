# 153. Módulos - import, from, as e *
'''
Python possuí muitos módulos padrão.
https://docs.python.org/pt-br/3/tutorial/modules.html
'''

# formas de importar um módulo:

'''
1) importar o módulo inteiro - import nome_modulo 
Vantagem: Precisa usar o namespace do módulo
Desvantagem: nomes grandes 
'''
import sys
#sys.exit() #saí do programa!
print(sys.platform) # mostra o kernel que estamos usando


'''
2) importar parte do módulo - from nome_modulo import objeto1, objeto2
Vantagem: nomes pequenos
Desvantagem: sem o namespace do módulo

OBS: Tem que tomar cuidado para não colocar nome da var igual do módulo
para não sobrescrever.
'''
from sys import exit, platform
#platform = 'casa'
print(platform)

'''
alias 1 - import nome_modulo as apelido (mudar o nome do módulo)
'''
import math as m
math = 10
print(m.sqrt(9))

'''
alias 2 - from nome_modulo import objeto as apelido
Vantagem: Pode reservar nomes para o código
Desvantagem: Pode ficar fora do padrão da linguagem
'''
from sys import platform as pf
print(pf)

'''
MÁ PRÁTICA - from nome import *
Vantagem/Desvantagem: Importa tudo de um módulo
'''
from sys import *












#desconsiderar(ver aula 154)
print('Esse módulo se chama', __name__)
