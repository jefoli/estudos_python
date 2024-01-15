# 84. Cuidados com tipos de dados mutáveis - list e copy (básico - só para entender o funcionamento)

lista_nome = ['Luiz', 'Marcos', True] # lista com valores mutáveis

lista_nome_b = lista_nome # Estamos passando os parâmetros por referência, logo ambos valores estão apontando para o mesmo local de memória.

lista_nome[0] = 'Lucas'

print(lista_nome_b)

# Para criar uma nova variável com os dados da lista, basta usilizar o método (copy):

lista_nome_c = lista_nome.copy()
print(f'{lista_nome_c=}')


# 85. for in com tipo list

lista = ['Maria', 'Helena', 'Fernando']

for nome in lista:
    print(nome, type(nome))