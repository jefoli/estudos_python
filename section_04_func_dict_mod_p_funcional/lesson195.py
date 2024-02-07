# 196. Positional-Only Parameters (/) e Keyword-Only Arguments (*)
'''
**args (disponibilizar um qtd ilimitada de argumentos posicionais)
**kwargs (disponibilizar um qtd ilimitada de argumentos nomeados)

PEP 570 Position-Only Parameters:
https://peps.python.org/pep-0570/

Position-Only Parameters (/) -
    - Tudo antes da barra deve ser SOMENTE arg posicional
    - colocar / na definição da função!
    - Dessa forma, evita de uma pessoa passar um argumento nomeado para função.

PEP 3102 - Keyword-Only Arguments
https://peps.python.org/pep-3102/s

Keyword-Only Arguments (*) - SOZINHO
    - Tudo depois do asterisco deve ser nomeado
    - limita a qtd de argumentos posicionais que temos,
    - porém podemos passar argumentos nomeados antes do *
    - * =! *args
'''

def soma(*args):
    print(sum(args))
soma(3,4,9)

# Position-Only Parameters (/)
def dividir (x, y, /):
    print(x//y)
dividir(3,3)

# podemos passasr parâmetros depois de (/)
# Porém muda na chamada, pois podemos passar um arg depois da barra
def multiplicar(a, b, /, c, d):
    print(a*b*c*d)
multiplicar(3,4, c=3, d=1)

# Keyword-Only Arguments (*) 
# tudo que vier depois do * deve ser arg nomeado
def subtrair(y, z, *, c):
    print(y - z - c)
subtrair(1, 2, c=3)


def somar_2(y, z, /, *, c):
    print(y - z - c)
somar_2(1, 2, c=3)