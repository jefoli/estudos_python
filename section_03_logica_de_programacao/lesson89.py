# 89. enumerate para enumerar valores de iteráveis (pegar índices)
# O enumerate tem a função de enumerar cada item de uma lista.

lista = ['Maria', 'José']
lista.append('Lucas')

for item in enumerate(lista):
    print(item)

# É possivel desempacotar c/ enumerate:

## 1 forma de desempacotamento (forma simplificada):
for indice, nome, in enumerate(lista):
    print(indice, nome)

# 2 forma:
for i in enumerate(lista):
    indice, nome = i
    print(indice, nome)
print('-' * 10)
