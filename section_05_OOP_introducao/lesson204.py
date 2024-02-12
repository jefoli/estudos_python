#204. Atributos de classe
'''
para acessarmos um atributo da classe em um método podemos utilizar

- nome da classe + atributo (recomendável)

- self + atributo (tomar cuidado) -> Ao utilizar self, 
por padrão irá entar buscar o valor na instância e depois na Classe.

OBS: Tomar cuidado ao alterar o valor de um atributo, 
pois poderá afetar o valor de todas as instâncias

'''

class Person:

    #atributo de classe:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        #Usamos Person p/ usar o atributo
        return Person.ano_atual - self.idade
        # return self.ano_atual - self.idade # ver OBS
    


p1 = Person('João', 35)
p2 = Person('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())