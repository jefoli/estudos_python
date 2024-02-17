# 223-224. Herança múltipla - Python Orientado a Objetos
'''
Quer dizer que em Python, uma classe pode estende várias outras classes.

Herança simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente

Herança múltipla e mixins(uma class que não faz parte daquela familia):

Animal -> Mamifero -> Humano -> Pessoa -> Cliente

Log -> FileLog

Cliente(Pessoa, FileLog) # mixin

Python 3 usa C3 superclass linearization para gerar o MRO.

Para saber a ordem de chamadas dos métodos, usar:
    - método de classe Classe.mro() ou 
    - atributo __mro__ (dunder mro)

EXTRAS:
article: https://en.wikipedia.org/wiki/C3_linearization

C3 linearization, also known as C3 superclass linearization, 
resolves conflicts when inheriting different definitions of the same property from multiple superclasses.

The goal is to obtain a deterministic order in which methods should be inherited.

Pesquisa: Problema do diamante
'''

class A:
    ...
    def quem_sou(self):
        print('A')

class B(A):
    ...
    #def quem_sou(self):
    #    print('B')

class C(A):
    ...
    def quem_sou(self):
        print('C')

class D(B, C):
    ...
    # def quem_sou(self):
    #    print('D')

d = D()
d.quem_sou()

print(D.mro()) # retorna o C3 linearization
#print(D.__mro__)