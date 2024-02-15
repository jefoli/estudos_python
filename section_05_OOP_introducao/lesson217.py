# 217. Composição - Python Orientado a Objetos
'''
Composição é uma especialização da agregação.
Quando o objeto "pai" for apagado, todas as ref. dos objetos
filhos também serão deletados.

Dica extra: Garbage Collector (GC) em Python é um mecanismo responsável pela gerência automática de memória. 
Ele aloca memória para objetos e a desaloca quando esses objetos não possuem mais referências.
'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        
        # Criamos a instância de Endereço na classe cliente:
        # Quando cliente deixar de existir, a instância tbm deixará de existir.
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente_1 = Cliente('Maria')
cliente_1.inserir_endereco('Avenida Brasil', 54)
cliente_1.inserir_endereco('Rua São João', 2312)
cliente_1.listar_enderecos()


