# 247-249. Teoria: metaclasses são o tipo das classes
"""
O que é Type? 
Type é uma metaclasse que controla o comportamento das classes.
Metaclasses são o tipo das classes.
A metaclasse padrão em Python é chamada de type.
Basicmaente type cria classes em python

Em Python, tudo é OBJETO (classes também).

Uma classe é um objeto especial que define a estrutura e o comportamento de 
outros objetos.

Assim, qual é o tipo de uma classe? -> type
Seu objeto é uma instância da sua classe!
Sua classe é uma instância de type (type é uma metaclasse)
Type gera o seguinte: type('Name', (Bases,), __dict__)

Ao criar uma classe, por padrão ocorre a seguinte ordem:
1) __new__ da metaclasse é chamado e cria uma nova classe
2) __call__ da metaclass é chamado com os argumentos e também chama:
    2.1) __new__ da classe com os argumentos (cria a instância)
    2.2) __init__ da class com os argumntos
3) __call__ da metaclasse termina e execução


Métodos importantes da metaclass:

__new__(mcs, name, bases, dct) - cria a classe
# bases = heranças em ordem 

__cal__ (cls, *args, *kwargs) - cria e inicializa a instância

OBS: Em Python podemos manipular a criação da class em (__new__), instância da metaclass (__call__)

"Metaclasses são magias mais profundas do que 99% dos usuários deveriam se preocupar. Se você quer saber se precisa delas, 
não precisa (as pessoas que realmente precisam delas sabem com certeza que precisam delas e não precisam de uma explicação sobre o porquê)."
— Tim Peters (CPython Core Developer)
"""

# object acima da class Foo
from typing import Any


class Foo:
    ...

f = Foo() #instância da classe
#print(isinstance(f, Foo))
print(type(f))
print(type(Foo))


# Exp criar uma classe utilizando Type (ordem de construção da class):
ExpType = type('ExpType', (object,),{})
e = ExpType()
print(type(ExpType))


# Exp p/ criar uma metaclass(cria a class)

def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type): 
    def __new__(mcs, name, bases, dct):
        print('Metaclass nova')
        cls = super().__new__(mcs, name, bases, dct)

        # Podemos executar tarefas antes da criação da classe em si:
        cls.attr = 1234

        # podemos colocar métodos dentro da metaclasse:
        cls.__repr__ = meu_repr

        # podemos fazer checagem/levantar exceção:

        # no exp abaixo, se a pessoa não definir o método falar em Pessoa gera erro:
        if 'falar' not in cls.__dict__:
            not callable(cls.__dict__['falar'])
            raise NotImplementedError ('Implemente Falar')

        return cls

    #call cria e chama o init na instância, pois é resp por tratar dos () dos argumentos
    def __call__(self, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print('dict da instância em si:', instancia.__dict__)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError ('Crie o Attr nome!')
        return instancia


#toda metaclasse precisa herdar de Type

# Pessoa == instância de Meta
class Pessoa(object, metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('New')
        instanca = super().__new__(cls)
        return instanca
    
    def __init__(self, nome):
        print('Meu INIT')
        self.nome = nome

    def falar(self):
        print('Falando...')


# p1 == instância de Pessoa
p1 = Pessoa('Marcio Treviso')
print(p1)
print(p1.attr)
print('repr', p1)