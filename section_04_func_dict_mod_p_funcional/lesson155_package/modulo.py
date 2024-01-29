
# dunder __all__
# quando a pessoa fizer um import com all (*) só irá o que está dentro de __all__
__all__= [
    'variavel',
]


variavel = 'import_all'

def somar(x, y):
    return x + y


'''Ocorre um erro, pois importamos o modulo 'b' dentro de módulo do package
e o python tenta carregar o módulo 'b', mas não vai encontrar já que o ponto
de vista (__main__) é arquivo lesson158.py'''

#from modulo_b import fala_oi

#DESSA FORMA, TODAS IMPORTAÇÕES RELACIONADAS AO SISTEMA TEM QUE SER RELACIONADAS AO MAIN!

#Para corrigir esse erro, basta ir no módulo_b e importar da seguinte forma:
#falar o nome do package + modulo

from lesson155_package.modulo_b import fala_oi


print(fala_oi())