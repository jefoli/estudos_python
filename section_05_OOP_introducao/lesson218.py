# 218. Exercício com classes e relações
'''
1) Crie uma classe Carro.
2) Crie uma classe Motor.
3) Crie uma classe Fabricante.

4) Faça a ligação entre Carro 'tem' Motor.
Obs.: Um motor pode ser de vários carros.

5) Faça a ligação entre Carro e Fabricante.
Obs.: Um fabricante pode fabricar vários carros.

Exiba o nome do carro, motor e fabricantes na tela.
'''
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, motor):
        self.nome_motor = motor

class Fabricante:
    def __init__(self, marca):
        self.fabricante = marca

bmw = Carro('BMW X6')
motor_bmw = Motor('V.8 M3')
fabricante_bmw = Fabricante('BMW')

bmw.motor = motor_bmw
bmw.fabricante = fabricante_bmw
print('Modelo:', bmw.nome,'| fabricante:', bmw.fabricante.fabricante, '| motor:', bmw.motor.nome_motor)


mercedes = Carro('Classe A')
motor_mercedes = Motor('2.0 APS')
fabricante_mercedes = Fabricante('Mercedes Benz')

mercedes.motor = motor_mercedes
mercedes.fabricante = fabricante_mercedes
print('Modelo:', mercedes.nome,'| fabricante:', mercedes.fabricante.fabricante, '| motor:', mercedes.motor.nome_motor)