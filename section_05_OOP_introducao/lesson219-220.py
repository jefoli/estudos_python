# 219-220. Herança, generalização e especialização
'''
Dicas:
Associação - um objeto utiliza outro objeto.
Agregação - Um objeto tem outro objeto.
Composição - Ele tem é também é dono de outro objeto (associação e agregação fica dentro de composição)

HERANÇA -> Permite que você estenda a funcionalidade de uma classe existente, 
criando uma nova classe que herda características e comportamentos da classe original.

Classe Base/Principal (Super Class/Base Class/Parent Class):
A classe (mais genérica) da qual outras classes herdam é chamada de classe base ou super classe.
Ela contém atributos e métodos comuns que podem ser compartilhados por várias classes derivadas.

Classe Derivada/Filha (Sub Class/Child Class/Derived Class):
Uma classe que herda da classe base é chamada de classe derivada ou sub classe.
Ela estende ou modifica a funcionalidade da classe base.
Pode adicionar novos atributos e métodos específicos.

Para herdarmos uma classe, é necessário colocar parênteses 
e colocar a superclasse dentro: class exp(SuperClass): 

info complementar: Por padrão classe herda superclasse Built-in Object do Python

Method resolution order(MRO) - Ordem que o py irá buscar met/obj/etc na classe. (usar help() para ver)

self.__class__.__name__ -> pega o nome da classe

Dica: Usar no máximo 3 níveis da herança no máximo para não ficar complexo.

extra: pesquisar Heranças vs Composição

'''

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, 'Classe:', self.__class__.__name__)


class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

cliente_1 = Cliente('Luiz', 'Otávio')
aluno_1 = Aluno('Margarete', 'Santos')

cliente_1.falar_nome_class()
aluno_1.falar_nome_class()