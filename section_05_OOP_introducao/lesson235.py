# 239. __new__ e __init__ em classes Python
'''

__new__ -> Método responsável por CRIAR e retornar um novo objeto.
Por isso, recebe cls.

__new__ -> DEVE retornar um novo objeto

Obs: O __new__ é chamado antes do __init__, dado o fato de ser o resp. por criar a instância.45

(mais utilizado) __init__ -> é o método responsável por INICIALIZAR a instância.
Por isso recebe, self.

__init__ -> NÃO DEVE retornar nada (None)!

lembre-se: object é a super classe de uma classe

Extra: new e init são similares a contrutores (método que cria um objeto) em outras linguagens.
'''

class A:

    def __new__(cls, *args, **kwargs):
        #podemos executar coisas antes de criar a instância
        print('Antes de criar a inst...')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o Init')

    def __repr__(self):
        return 'A()'

a = A(333)
print(a.x)
print(a)