# 230. abstractmethod para qualquer método já decorado (property e setter)
'''
Abstractmethod para qualquer método já decorado
É possível criar @property @property.setter @classmethod
@staticmethod e métodos normais como abstratos, para isso use
@abstractmethod como decorator mais interno.

Dica: Foo - Bar, são palavras usadas como placeholder para 
palavras que podem mudar na programação (pode ser qualquer coisa)

@abstractmethod deve vir o mais interno possível

Documentação: https://docs.python.org/3/library/abc.html
'''

from abc import ABC, abstractmethod

# Não é abstrata pq não tem nenhum método abstrato
class AbstractFoo(ABC):

    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self): ...


# classe concreta(vai ser usada):
class Foo(AbstractFoo):
    
    def __init__(self, name):
        super().__init__(name)
        #print('Só repasso a chamada p/ AbstractFoo')


    # 1) forma:
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # 2) forma:
    # Se criarmos um atributo de classe irá funcionar, mas perde o setter.
    # name = ''

    # Forma de settar um 

foo = Foo('Bar')

print(foo.name)


# exp com um setter abstrato

class AbstractFoo(ABC):

    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self): ...


# @property.setter - classe concreta(vai ser usada) :
# Para isso, usar o namespace da classe que estamos herdando
class SetterAbstrato(ABC):
    
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

class DefinirSetter(SetterAbstrato):
    
    def __init__(self, name):
        super().__init__(name)

    @SetterAbstrato.name.setter
    def name(self, name):
        self._name = name


definir_setter = DefinirSetter('Setter Definido')

print(definir_setter.name)