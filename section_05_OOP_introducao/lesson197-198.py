#197-198. class - Classes são moldes para criar novos objetos
'''
Dicas de livros:
    - Padrões de Projeto(Design Patterns): Soluções reutilizáveis 

class - Classes são moldes para criar novos objetos

As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.

Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.

CONVENÇÃO: PascalCase para nomes de classes.

Dicas: 
- dados dentro da classe são chamados de 'atributos'.
- ações dentro da classe são chamados de 'métodos'.

Conhecimentos extras:

callable() é uma função embutida que podemos usar para verificar se um objeto é “chamável”, 
ou seja, se ele pode ser chamado como uma função. 
Essa função geralmente retorna True se o objeto puder ser chamado e False caso contrário.

'''

#Criar uma classe:
class Person:
    ...
p1 = Person()
p1.nome = 'Monte'
p1.sobrenome = 'Olivier'
print(p1.nome) # por ser dados, não recebe -> (), pois se tornaria callable
print(p1.sobrenome)

p1 = Person()
p1.nome = 'Monte'
p1.sobrenome = 'Olivier'