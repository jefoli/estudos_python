# 236-237. Teoria: python Special Methods, Magic Methods ou Dunder Methods
"""
Dunder = Double Underscore = __dunder__
Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.htmlpecialnames
__init__(self, other) 
__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other (O método __gt__ é uma implementação do operador maior que (>))
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str (representação do objeto)

Dica1: __repr__ -> + voltado para devs (comunicação de como o objeto seja criado/montado) 
para saber a parte de desenvolvimento do objeto

Dica2: __str__ -> representação de uma string do objeto
"""

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'Ponto({class_name}(x={self.x!r}), y={self.y!r}, z={self.z!r})'

p1 = Ponto(1,2)
p2 = Ponto(30,455)

print(p1)

#para ver o repr:
print(repr(p2))
print(f'{p2!r}')