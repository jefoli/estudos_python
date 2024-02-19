# 238. Exemplo de uso de dunder methods (métodos mágicos)

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'Ponto({class_name}(x={self.x!r}), y={self.y!r}, z={self.z!r})'

    # +
    def __add__(self, other):
        novo_x = self.x + other.x #(4, 6)
        novo_y = self.y + other.y #(2, 4)
        return Ponto(novo_x, novo_y)
    
    # >
    def __gt__(self, other):
        resultado_self = self.x + self.x
        resultado_other = other.y + other.y
        return resultado_self > resultado_other

if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)

    p3 = p1 + p2 # chama __add__ 
    print(p3)

    print('P1 é maior que P2?', p1 > p2) # chama __gt__
    print('P2 é maior que P1?', p2 > p1) # chama __gt__