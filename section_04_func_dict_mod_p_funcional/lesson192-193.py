# 192-193. Exercício - Lista de tarefas com opções de desfazer e refazer
'''
- criar uma lista

- criar um input para o usuário digitar coisas
    - ele pode digitar tarefas ou comandos
    - comandos:
        - listar (tarefas)
        - desfazer (última operação)
        - refazer (última operação)

Dica: Explica o problema em voz alta e o problema de programação!
    - temos que criar uma lista de tarefas ...

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

https://en.wikipedia.org/wiki/Rubber_duck_debugging
'''

todo_list = []
deleted_items = []
desfazer = []

# 1) resposta sem funções:
while True:
    menu_options = input('ESCOLHA UMA OPÇÃO: \n| CADASTRAR | MOSTRAR | EXCLUIR | DESFAZER | REFAZER | LIMPAR: ').strip()

    if menu_options == 'CADASTRAR':
        receive_item = input('Digite a tarefa que deseja cadastrar: ')
        todo_list.append(receive_item)

    elif menu_options == 'EXCLUIR':
        if len(todo_list) == 0:
            print('Lista Vazia')
        else:    
            delete_item = input('Digite a tarefa que deseja excluir: ')

            if delete_item in todo_list:
                item_removed = todo_list.remove(delete_item)
                print('Item removido da lista:', delete_item)
                deleted_items.append(delete_item)

    elif menu_options == 'LIMPAR':
        clear_list = input('Você tem certeza que deseja limpar lista? [S]im ou [N]ão:').lower().strip()
        
        if clear_list.startswith('s'):
            del_all_list = todo_list.clear()
            print('Lista Limpa!')
        else:
            print('retornando ao menu inicial')

    elif menu_options == 'DESFAZER':
        if len(deleted_items) == 0:
            print('Lista vazia')
        else:
            todo_list.append(deleted_items[-1])
            desfazer.append(deleted_items.pop())

    elif menu_options == 'REFAZER':
        if len(desfazer) == 0:
            print('Lista vazia')
        else:
            if desfazer[0] in todo_list:
                todo_list.pop()
        
    elif menu_options == 'MOSTRAR':
            for item in sorted(todo_list):
                print(item)
    else:
        print('Opção inválida!')
        break


# 2) resposta com funções:
import os

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    print()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    tarefas.append(tarefa)

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer_tarefa(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    remover_tarefa = tarefas.pop()
    print(f'{remover_tarefa=} removida da lista')
    tarefas_refazer.append(remover_tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    refazer_tarefa = tarefas_refazer.pop()
    print(f'{refazer_tarefa=} adicionada na lista de tarefas.')
    tarefas.append(refazer_tarefa)
    print()

tarefas_todo = []
tarefas_refazer = []

while True:
    print('Comandos: listar | desfazer | refazer | limpar')
    tarefa_input = input('Digite uma tarefa ou comando: ')

    if tarefa_input == 'listar':
        listar(tarefas_todo)
    
    elif tarefa_input == 'desfazer':
        desfazer_tarefa(tarefas_todo, tarefas_refazer)
        listar(tarefas_todo)
    
    elif tarefa_input == 'refazer':
        refazer(tarefas_todo, tarefas_refazer)
        listar(tarefas_todo)
    
    elif tarefa_input == 'limpar':
        os.system('cls') # cls (windows), clear (mac/linux)
    else:
        adicionar(tarefa_input, tarefas_todo)
