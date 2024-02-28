# 84. Cuidados com tipos de dados mutáveis - list e copy (básico - só para entender o funcionamento)

lista_com_val_mutaveis = ['Luiz', 'Marcos', True] # lista com valores mutáveis

copia_lista_com_val_mutaveis = lista_com_val_mutaveis # Estamos passando os parâmetros por referência, 
# logo ambos valores estão apontando para o mesmo local de memória.

#vars com mesmo endereço de memória:
print('end. memória lista_com_val_mutaveis:', id(lista_com_val_mutaveis))
print('end. memória copia_lista_c_val_mutaveis:', id(copia_lista_com_val_mutaveis))


lista_com_val_mutaveis[0] = 'Lucas'
print(copia_lista_com_val_mutaveis)

# Para criar uma nova variável com os dados da lista, basta utilizar o método (copy):
lista_com_copy = lista_com_val_mutaveis.copy()
print(f'{lista_com_copy=}')


# 85. for in com tipo list
lista = ['Maria', 'Helena', 'Fernando']

for nome in lista:
    print(nome, type(nome))