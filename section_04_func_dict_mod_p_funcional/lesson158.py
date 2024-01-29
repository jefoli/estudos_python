# 158. O ponto de vista do __main__ pode te confundir em módulos e pacotes Python
'''
- todo arquivo executado como main! -> print(__name__)
é comum ter módulo com nomes similares dentro de packages
'''

'''Ocorre um erro, pois importamos o modulo 'b' dentro de módulo do package
e o python tenta carregar o módulo 'b', mas não vai encontrar já que o ponto
de vista (__main__) é arquivo lesson153.py'''

from lesson155_package.modulo import somar

print(__name__)

#DESSA FORMA, TODAS IMPORTAÇÕES RELACIONADAS AO SISTEMA TEM QUE SER RELACIONADAS AO MAIN!

#Para corrigir esse erro, basta ir no módulo_b e importar da seguinte forma:
#falar o nome do package + módulo (VER arq.módulo)