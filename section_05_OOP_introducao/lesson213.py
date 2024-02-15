#213. @property + @setter - getter e setter no modo Pythônico
'''
Geralmente utilizado nas seguintes situações:
    - como getter
    - P/ evitar quebrar o código cliente
        - Código que usa o seu código/classe!!!
    - P/ habilitar setter
    - P/ executar ações ao obter um atributo

Setter - método utilizado para CONFIGURAR determinado atributo

CONVENÇÃO: quando criarmos um atributo e inserirmos um _ ou __ (_atributo),
quer dizer que aos outros devs que esse atributo NÃO deve ser usado,
pois é um atributo interno da classe.
Seria igual dizer que o atributo está private ou protected

# PRIVATE | PROTECTED | PUBLIC

@setter O seter é um método que tem que ter o self + receber um valor

Obs: Podemos passar o getter diretamente como param. 

'''
class Caneta:
    def __init__(self, color):
        # convenção (_)
        # private protected:
        self._color = color
        self._cor_tampa = None

    #getter (obter valor):
    @property
    def cor_caneta(self):
        return self._color

    #setter (config. valor):
    @cor_caneta.setter
    def cor_caneta(self, value):
        if value == 'Transparente':
            raise ValueError('Não não aceita!')
        print('Setando cor:', value)
        self._color = value

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Vermelha')

# getter -> obter um valor:
print('Caneta:', caneta.cor_caneta)

# setter -> Config. valor
# O valor vai p/ o setter
caneta.cor_caneta = 'Rosa'
#caneta.cor_caneta = 'Transparente'

caneta.cor_tampa = 'Verde'

print('Caneta:', caneta.cor_caneta)
print('Tampa:', caneta.cor_tampa)
