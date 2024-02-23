# 221-222. super e a sobreposição de membros em Python Orientado a Objetos
"""
Podemos sobrepor o valor de uma classe.

super() - É uma classe, cuja função é retornar temporariamente a superclasse,
dessa forma, podemos chamar métodos da superclasse.

B.metodo(self) -> teria mesma função de super, não é recomendável!!!

.mro() - Method resolution order (lista de order)
"""

# str -> é uma classe built-in em Python
class MinhaString(str):

    # fizemos a sobreposição do método upper
    def upper(self):
        
        #podemos executar algo antes:
        print('Chamou Upper: ')

        #Retornamos o upper() que está vindo da classe super (str)
        return super().upper()

string = MinhaString('Luiz')
print(string.upper())
print()

class A:
    atributo_a = 'valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    
    #sobrepõe o init da class A
    def __init__(self, atributo, atr_b):
        
        # Chama os objetos do A p/ inicializar os objetos em B
        super().__init__(atributo)
        
        # podemos definir outra coisa em B no init
        self.atr_b = atr_b
    
    # método sobrepondo (a)
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Passei pelo C')

    # esse metodo está sobrepondo aos demais (A, B)
    def metodo(self):
        
        super().metodo() # super(classe acima) == B

        super(B, self).metodo() # super(classe acima) == A
        
        # super(A, self).metodo() # super(classe acima) == object

        print('C')

c = C('Atributo A', 'Atributo B')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo() # Executou o super

# executa 
print(c.atributo)
print(c.atr_b)

print(C.mro()) # Method resolution order