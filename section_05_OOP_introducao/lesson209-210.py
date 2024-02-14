#209-210. @staticmethod (métodos estáticos) são inúteis em Python =)
'''
@staticmethod (métodos estáticos) são métodos em que estão dentro da classe,
mas não tem acesso ao 'self' nem ao 'cls'.

Em resumo, são funções que existem dentro da sua classe.
'''

class Classe:
    @staticmethod
    def funcao_dentro_da_class(*args, **kwargs):
        print('Hello', args, kwargs)

c1 = Classe()
c1.funcao_dentro_da_class()
c1.funcao_dentro_da_class(1,2,3)
c1.funcao_dentro_da_class(arg_nomeado = 20)