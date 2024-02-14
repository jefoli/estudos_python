# 212. @property - um getter no modo Pythônico
'''
getter - É um método utilizado para obter um conteúdo

Modo pythônico: Modo do Python peculiar de fazer as coisas...

@property é uma propriedade do objeto, ela é um método que se comporta como ATRIBUTO
    - Não precisa colocar parenteses para chamar o método!

Geralmente utilizado nas seguintes situações:
    - como getter
    - P/ evitar quebrar o código cliente
        - Código que usa o seu código/classe!!!
    - P/ habilitar setter
    - P/ executar ações ao obter um atributo

Podemos alterar os métodos da classe e não irá quebrar o código do cliente!

'''

# Getter em Python:
class Pen:
    def __init__(self, color):
        self.color = color

    @property
    def colors(self):
        print('Property: ')
        return self.color
    
    @property
    def pen_cap(self):
        return 'White'

pen = Pen('Blue')
print(pen.colors)
print(pen.pen_cap)



# Getter(padrão) - semelhante em outras linguagems:
class Caneta:
    def __init__(self, cor):
        self.cor = cor

    # getter - protegemos o atributo de cor.
    def get_cor(self):
        print('Get COR')
        return self.cor
        
caneta = Caneta('Azul')
print(caneta.get_cor())