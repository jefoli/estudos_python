# 207-208. Métodos de classe (@classmethod) + factories methods (métodos fábrica)
'''
São métodos onde 'self' será 'cls, ou seja, 
ao invés de receber a instância no primeiro parâmetro,
recebemos a própria classe!

@classmethod: é um Decorator Tem a função de chamar o método sem a necessidade de passar o self!
    - No entanto, é necessário receber a própria classe como param, por isso usamos 'cls'
    - utilizado para criar factories métodos
    - nesse caso estamos chamando diretamente a classe dentro do class method
    - dica: seria como se fosse uma extensão do molde
'''

class Pessoa:
    ano = 2023 #atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #method de decorator
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


#print(Pessoa.ano)
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(30)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
#Pessoa.metodo_de_classe()