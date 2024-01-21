# 116. Closure e funções que retornam outras funções
"""
Em Python, um closure (fechamento) refere-se a uma função que "encapsula" variáveis do escopo em que foi definida, 
permitindo que a função tenha acesso a essas variáveis mesmo quando é chamada fora desse escopo. 
Em outras palavras, um closure é uma função que "lembra" do ambiente em que foi criada. 
Isso é especialmente útil quando você precisa preservar o estado de variáveis entre chamadas sucessivas da função.

"""

def criar_saudacao(saudacao):
    
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    
    return saudar

retornar_bom_dia = criar_saudacao('Bom dia')
retornar_boa_noite = criar_saudacao('Boa noite')

print(retornar_bom_dia('Luiz')) #closure
print(retornar_boa_noite('Luiz')) #closure

lista_nomes = ['Yuri', 'Felipe', 'Elionay']

for nome in lista_nomes:
    print(retornar_bom_dia(nome))