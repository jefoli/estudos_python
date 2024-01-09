# 43. Operadores in e not in

# in = está entre
# not in = não está entre

# String em python são iteráveis (podemos navergar item por item)

# 0 1 2 3 4 5 (índice)
# o t a v i o (palavra que queremos iterar)
#-6-5-4-3-2-1 (iterar de trás para frente usando negativo)

nome = 'Otavio'
print(nome[2]) 
print(nome[-4])

# vamos checar letra por letra utilizando IN

print('a' in nome) # isso é uma condição (retorna true or false)
print('vio' in nome)
print('vio' not in nome) # False, poir está na var

nome = input('Digite o nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print('Não localizado')