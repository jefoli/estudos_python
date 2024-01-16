# 94. Listas dentro de listas (iteráveis dentro de iteráveis)
# Podemos ter listas dentro de listas, bem como acessar tais valores!

salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],
]

print(salas)
print(salas[0][1])
print(salas[1][0])
print(salas[2][2])
print(salas[2][-1][2]) # 20


for sala in salas:
    for item in sala:
        print(item)

