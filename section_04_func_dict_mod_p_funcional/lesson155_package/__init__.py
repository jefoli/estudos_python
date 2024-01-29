print(
    'você importou', __name__
)

def dobrar_valor(x):
    return x * 2

from lesson155_package.modulo import somar, variavel

# Um dos poucos casos que podemos importar all (*) seria no __init__ sem causar problemas
from lesson155_package.modulo_b import *