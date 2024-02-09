# 202. Escopo da classe e de métodos da classe
'''
- Classes tem escopos
- Métodos de função também tem escopos
'''

class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel_escopo_interno = 'Valor qualquer'
        print(variavel_escopo_interno)

    def alimentar(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.alimentar(*args, **kwargs)


leao = Animal('Leão')
print(leao.nome)
print(leao.alimentar('Laranja'))
print(leao.executar('Carne'))