# 91. Sugestão de solução do exercício - crie uma lista de compras com listas (com try / except)
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Digite o item que deseja adicionar: ')
        lista.append(item)
            
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Escola o índice que deseja apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido!')

    elif opcao == 'l':  
        os.system('cls')
        if len(lista) == 0:
            print('lista vazia.')
        
        for i, valor in enumerate(lista):
            print(f'Itens da lista:\n{i, valor}')

    else:
        print('Por favor, escolha uma das opções [i], [a] ou [l]')