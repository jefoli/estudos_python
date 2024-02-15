# 215. Relações entre classes: associação, agregação e composição
'''
Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos, 
como agregação e composição.

Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
'''

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        
        #associação:
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

#associação:
#escritor.ferramenta = caneta
escritor.ferramenta = maquina_de_escrever # se não fizer essa ligação, dará erro (None)

print(caneta.escrever()) #
print(escritor.ferramenta.escrever()) #usando a associação do escritor