# 126-127. Introdução ao tipo set em Python (conjuntos)
'''
Sets conjuntos em python (tipo set)

Sets são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

formas de cria um set:
    1) set():
    2) {1, 2, 3}
        - Obs(1): É necessário colocar valores dentro de {}, caso contrário seja criado um dicionário! Para cria um set vázio -> var = {''}

Dicas:
    - Sets são eficientes para remover valores duplicados de iteráveis.
    - Seus valores serão sempre únicos, logo não haverá repetidos.
    - Não aceitam valores mutáveis.
    - Não possuem índex, logo não podemos acessar um valor pelo index
    - Não garantem a ordem das informações.
    - São iteráveis (for, in, not in)
'''

#formas de criar sets

#1 forma - class set():
primeira_forma_set = set()
print(primeira_forma_set, type(primeira_forma_set))

# 2 forma - set c/ chaves:
segunda_forma_set = {''} #Obs(1)
print(segunda_forma_set, type(segunda_forma_set))

exp_set = {'Luiz', 1, 2, 3, (4,5,6,)}
print(exp_set)
print()

# remove os valors duplicados:
exp_set_2 = {1,2,4,5,6,7,7,7,8,8,8,8,8,8,8}
print(exp_set_2)
print()

#tratando uma lista:
lista_1 = [1,2,3,4,5,5,6,6,2,2,3,4]
tratar_lista = set(lista_1)
lista_tratada = list(tratar_lista)
print(lista_tratada)
print()

# For, In, not In
verificar_num = 3 in exp_set
verificar_palavra = 'Casa' not in exp_set
print('Número 3 está no set:', verificar_num)
print('Casa NÃO está no set:', verificar_palavra)

for num in exp_set:
    print(num)

print()
