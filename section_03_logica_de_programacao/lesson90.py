# 90. Exercício - crie uma lista de compras com listas
"""
1) Faça uma lista de compras com listas

Observações: 
O usuário deve ter a possibilidade de:
    inserir, 
    apagar e listar 
    valores de sua lista.

Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:

    menu = input(f'Escola uma opção: \n[1] Inserir item \n[2] Listar item'\
                f'\n[3] apagar item \n[4] Sair \n -> ')

    if menu == '1':
        os.system('cls') # 'cls' p/ windows | 'clear' p/ linux
        add_item = input('Insira o item que deseja comprar: ')

        if len(add_item) == 0:
            print('Digite corretamente o item que deseja adicionar!')
        
        lista_de_compras.append(add_item)
    
    elif menu == '2':
        os.system('cls')
        for i in enumerate(lista_de_compras):
            print(i)
    
    elif menu == '3':
        os.system('cls')
        excluir_item = input('Qual Produto deseja excluir?: ')

        for i, j in enumerate(lista_de_compras):
            if excluir_item == j:
                lista_de_compras.remove(j)
    
    elif menu == '4':
        print('Você saiu do programa! Até Logo!!!')
        break
    
    else:
        print('Opção inválida!')
