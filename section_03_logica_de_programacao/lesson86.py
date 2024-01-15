# 86. Exercício - exiba os índices da lista (aula com solução)

''' Exiba os índices da lista'''


lista = ['Maria', 'Helena', 'Fernando']

# 1 forma
for nome in enumerate(lista):
    print(nome)

# 2 forma
for name_list in lista:
    print(lista.index(name_list), name_list)


# 3 forma 
    
indices = range(len(lista))

for i in indices:
    print(i, lista[i])