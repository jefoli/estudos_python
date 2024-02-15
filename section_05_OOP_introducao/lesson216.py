# 216. Agregação - Python Orientado a Objetos
'''
Agregação é uma forma especializada de associação entre dois objetos.

Cada objeto terá seu ciclo de vida independente.

Geralmente é uma relação de UM para MUITOS, onde um objeto tem
um ou vários objetos.
Exp: Um veículo pode ter 1 ou várias rodas.

Os objetos podem viver separadamente, mas pode se tratar de uma relação
onde um objeto precisa de outro para fazer determinada tarefa.

Obs: Exitem controvérsias sobre definições de agregação.
'''

class CarrinhoDecompras:
    def __init__(self):
        #agregação:
        self._produtos = []

    def inserir_produtos(self, *produtos):

        #alternativas p/ inserir produtos:
        
        # 1:
        self._produtos.extend(produtos)
        
        # 2:
        #self._produtos += produtos

        # 3:
        #for produto in produtos:
        #    self._produtos.append(produto)

    def total(self):
        return sum([p.preco for p in self._produtos]) 
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = CarrinhoDecompras()

p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 30)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print('total:', carrinho.total())