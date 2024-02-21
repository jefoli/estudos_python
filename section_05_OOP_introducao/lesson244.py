# 244. Funções decoradoras e decoradores com métodos

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} ({class_dict})'
    return class_repr

def adicionar_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def meu_pais(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if 'Mongólia' in resultado:
            return 'Você chegou a seu destino!'
        return resultado

    return interno


@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    
    def falar_nome(self):
        return f'O time é {self.nome}'

@adicionar_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome

    @meu_pais
    def falar_nome(self):
        return f'O País é {self.nome}'


brasil = Time('Brasil')

mongolia = Pais('Mongólia')
suica = Pais('Suiça')

print(brasil)
print(mongolia)

print(suica.falar_nome())
print(mongolia.falar_nome())