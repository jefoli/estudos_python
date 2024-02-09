# 201. Entendendo self em classes Python
'''
- self -> é um nome dado por convenção, para referenciar a própria instância.

- Deve ser SEMPRE o primeiro parâmetro!

- Uma classe pode gerar várias instâncias
'''

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def imprimir_self(self):
        print(f'Atributos da instância:\n{self.nome=}\n{self.sobrenome=}')
        print(f'Valor da instância {self=}')

lucas = Pessoa('Lucas', 'Bernardo')
lucas.imprimir_self()
print(f'Valor do atributo {lucas=}\n')