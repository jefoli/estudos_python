# 74. Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)
'''
Iterável - É um elemento que possui um método chamado (__iter__) - itera sobre string, range, etc

Iterador: Quem sabe entregar um valor por vez

next: Entrega o próximo valor

iter: Entrega o valor do iterador

'''

#iter - entrega um objeto iterador que sabe iterar a string
text = 'luz'.__iter__() # Não precisamos digitar isso, pois o python já possui uma função chamada iter()
text = iter('luz') # = __iter_()
print(text)

# next - chama o próximo valor que está disponível no iter.
#Obs: quando esgota os valores, um erro é levantado
print(text.__next__()) # Python já tem uma função que chama o next.
print(next(text)) # = __next__()


n1 = range(0, 100, 8)


# Por trás do FOR:
exp_while_for = 'Example'
iterator = iter(exp_while_for)
while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break


# Mesma função utilizando for:
for ltr in exp_while_for:
    print(ltr)
