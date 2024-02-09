#200. Métodos em instâncias de classes Python
# Não se esqueça: Classe é um molde que gera novas instâncias/objetos
# Método -> é uma função dentro da classe.

class Car:
    #inicializar um objeto:
    def __init__(self, name):
        self.name = name

    # método:
    def speed_up(self):
        print(f'{self.name} está acelerando...')

fusca = Car('Fusca')
print(fusca.name)
fusca.speed_up()

celta = Car(name = 'Celta')
print(celta.name)
celta.speed_up()