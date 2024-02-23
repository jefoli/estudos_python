# 229. Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos
"""
Classes abstratas - Abstract Base Class (ABC)

As ABCs são classes base abstratas que fornecem uma estrutura para definir interfaces 
e comportamentos comuns.

ABCs são usadas como contratos para a definição de novas classes.

Elas não podem ser instanciadas diretamente, mas servem como modelos para outras 
classes.

Elas podem forçar outras classes a criarem métodos concretos.

Também podem ter métodos concretos por elas mesmas.

@abstractmethods -> são métodos que não tem corpo.

As regras para as classes abstratas com métodos abstratos é que elas
NÃO PODEM ser instânciadas diretamente!

-> Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod)

Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

É possível criar @property @setter @classmethod @staticmethod e @method como abstratos,
para isso use @abstractmethod como decorator mais interno.

Padrão de projeto (Abstract Factory): https://refactoring.guru/design-patterns/abstract-factory/python/example

OBS: Temos que importar a class ABC

formas de criar uma classe abstrata:
from abc import ABC, ABCMeta

1) class log(ABC):

2) class Log(metaclass = ABCMeta):

# Documentação: https://docs.python.org/3/library/abc.html
"""

from abc import ABC, abstractclassmethod

# forma mais conveniente:
class Log(ABC):

    #método abstrato:
    @abstractclassmethod
    def _log(self, msg): ...


#subclasse
class LogWithMixin(Log):
    
    def _log(self, msg):
        print(msg)

l = LogWithMixin()