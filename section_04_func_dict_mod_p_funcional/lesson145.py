# 145. Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
"""
Iterator = Fornece uma maneira de acessar sequencialmente um objeto agredado,
sem expor sua reprentação subjacente

responsabilidade do iterator -> saber o próximo valor!
- Não tem índice
- não dá para saber o tamanho do iterator!

OBS: O iterator esgota os valores e o pontiero para no último.

"""
iterable = ['EU', 'Tenho', '__iter__']

# podemos utilizar o método:
iterator_1 = iter(iterable) # tem __ter__ e __next__

# podemos chamar com o dander:
iterator_2 = iterable.__iter__() 

print(next(iterator_1))
print(next(iterator_2))
