# 64-65. Exercício guiado com while
# iterar strings com while + inserir *(asterisco) após cada letra

name = 'Luiz Fernando'
indice = 0
new_name = ''

# 1 forma
while indice < len(name):
    #print(name[indice]) # para ver o iterável
    new_name += f'*{name[indice]}'
    indice += 1
print(new_name)

# 2 forma
while indice < len(name):
    letter = name[indice]
    new_name += f'*{letter}'
    indice += 1
new_name += '*'
print(new_name)
