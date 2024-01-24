# 139. List comprehension com mais de um for

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)

# for dentro de for c/ list
lista_2 = [
    (x, y) for x in range(3)
    for y in range(3)
]
print(lista_2)

#list comprehension dentro de um valor de outra list
lista_3 = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
print(lista_3)