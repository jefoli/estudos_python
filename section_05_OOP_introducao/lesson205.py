# 205. __dict__ e vars para atributos de instância
'''
- mantém os valores que podem ser escritos dentro do objeto

__dict__ -> Os valores das instância estão salvos aqui

vars -> função para mostrar o __dict__ do objeto

OBS: O __dict__ é editável.

'''

class Person:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Person.ano_atual - self.idade
    
p1 = Person('João', 35)

p1.__dict__['nome'] = 'Nome alterado'

#podemos deletar:
#del p1.__dict__['idade']

print(p1.nome)

print('dict', p1.__dict__)

print('vars', vars(p1))