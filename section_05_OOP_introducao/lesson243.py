# 243. Funções decoradoras e decoradores (syntax sugar) com classes
# Uma classe sem __rep__ mostra somente o nome da classe e seu endereço de memória

# c/ decorador:
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr

# func que recebe uma classe.
def adiciona_repr(cls):
    # passamos para __repr__ uma ref. da func que estamos utilizando
    cls.__repr__ = meu_repr 
    return cls


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


# c/ herança:
class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr

class Time(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome

# retorno c/ herança
brasil = Time('Brasil')
portugal = Time('Portugal')
print(brasil)
print(portugal)
print('-'*30)
terra = Planeta('Terra')
marte = Planeta('Marte')
print(terra)
print(marte)
