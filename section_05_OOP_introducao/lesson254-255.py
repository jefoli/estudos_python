# 254-255 Teoria: enum.Enum (Enumerações)
"""
Enum -> Enumerações
Enumeração na programação, são usadas em ocasiões onde temos um determinado num
de coisas.

Enums tem membros e seus valores SÃO CONSTANTES.

Enums em Python:
    - são os conjunto de nomes simbólicos (membros) ligados a valores únicos
    - podem ser iterados para retornar seus membros canônicos na ordem de def.

enum.Enum -> é a superclasse para suas enumerações, mas também pode ser passada
diretamente (mesmo assim, Enums não são classes normais em Py).

Você poderá usar seu Enum com type annotations | isinstance | e outras coisas
relacionada com tipo.

Para obter os dados:
    chave = Classe.chave.name (obtém só o valor da chave)
    
    membro = Classe(valor) ou Classe['chave'] (obtém o valor do membro)
    - por valor(enumeração em sí), ele inicia a partir do 1
    
    valor = Classe.chave.value 

temos que importar o módulo!

Fácil de usar onde temos um grupo de coisas!
"""
import enum

#1) forma de criar enum:
# problema disso é que não fica com o type explicito.
Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

#formas de pegar os valores:

# MEMBRO INTEIRO:
# Membro valor (enumeração em si):
print(Direcoes(1))

# Membro chave:
print(Direcoes['DIREITA'])

print(Direcoes.ESQUERDA)

# Tipamos a direção para facilitar.
def mover(direcao: Direcoes):
    
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    print(f'Movendo para {direcao}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
# mover('lado')
print()

# 2) Forma de criar enum: interessante de utilizar o Enum para ficar mais explicito
class Directions(enum.Enum):
    RIGHT = enum.auto() 
    LEFT  = enum.auto() 

def walk(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direction.name} {direction.value}')

walk(Directions.LEFT)
walk(Directions.RIGHT)