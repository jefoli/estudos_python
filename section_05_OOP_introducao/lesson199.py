# 199. Introdução ao método __init__ (inicializador de atributos)
'''
O método __init__ é um método especial em Python que é chamado 
utomaticamente quando você cria uma instância (objeto) de uma classe.

Ele é usado para inicializar os atributos (variáveis) do objeto.

O nome __init__ é uma convenção e não deve ser alterado.

OBS: Todo método que for tratar uma instância precisa receber 'self' como primeiro parâmetro!

self -> O parâmetro self é uma referência ao próprio objeto (instância) que está sendo criado.
Ele é usado para acessar os atributos e métodos do objeto dentro da classe.
O nome self é uma convenção,mas você pode usar qualquer outro nome (embora não seja recomendado).
'''

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

car_1 = Car('La Ferrari', 'Ferrari')
print('Name:', car_1.name)
print('Brand:', car_1.brand)