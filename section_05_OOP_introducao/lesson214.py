# 214. Encapsulamento (modificadores de acesso: public, _protected, __private)
'''
Python NÃO TEM modificadores de acesso, 
mas podemos seguir as seguintes convenções:
    
(sem underline) = public
    - pode ser acessado em qualquer lugar (dentro/fora) da class

_ (um underline) = protected
    - NÃO deve ser usado fora da classe ou subclasses.

__ (dois underlines) = private
    "name mangling" (desfiguração de nomes) em Python
    - SOMENTE usar na classe em que foi declarado.
    - NÃO USAR em subclasse.

Mais infos na PEP 8 - https://peps.python.org/pep-0008/

Dentro da classe, podemos usar em qualquer lugar protected e private
'''

# public
class ExamplePulic:
    def __init__(self):
        self.public = 'Isso é público'

    def metodo_publico(self):
        return 'metodo_publico'

example_public = ExamplePulic()
print(example_public.public)
print(example_public.metodo_publico())
print()

# protected
class ExampleProtect:
    def __init__(self):
        # _ == protected
        self._protected = 'Isso é protegido'

    def _metodo_protected(self):
        return '_metodo_protected'

exp_protected = ExampleProtect()

# Apenas exp: NÃO USAR fora da classe!
print(exp_protected._protected) 
print(exp_protected._metodo_protected()) 
print()

# private
class ExamplePrivate:
    def __init__(self):
        # __ == private
        self.__private = 'Isso é private'

    def __metodo_private(self):
        return '__metodo_private'

exp_private = ExamplePrivate()

# NÃO VAI RETORNAR VALOR:
print(exp_private.__private)
print(exp_private.__metodo_private())