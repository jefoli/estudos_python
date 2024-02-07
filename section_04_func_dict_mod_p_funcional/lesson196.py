# 195. Exercício - salvando a lista de tarefas em JSON
# Criar sistema de lista de tarefas e criar um JSON para salvar as infos

import json

def cadastrar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    tarefas.append(tarefa)
    print()

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar!')
        print()
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(tarefa)
    print()

def desfazer(tarefa, desf_tarefa):
    print()
    if not tarefa:
        print('Não há itens para refazer!')
        return
    remover_tar = tarefa.pop()    
    desf_tarefa.append(remover_tar)
    print()

def refazer(tarefa, ref_tarefa):
    print()
    if not ref_tarefa:
        print('Não há itens para refazer!')
        return
    refazer_tar = ref_tarefa.pop()    
    tarefa.append(refazer_tar)
    print()

def ler(tarefas, path):
    data = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    
    except FileNotFoundError:
        print('Arquivo não existe!')

        # Cria o arquivo se não existir
        salvar(tarefas, path) 
    return data

def salvar(tarefas, path_arq):
    dados = tarefas
    
    with open(path_arq, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    
    return dados

PATH_ROUTE = 'lesson196.json'
tarefas = ler([], PATH_ROUTE)
desfazer_tarefas = []

while True:

    print('Comandos: cadastrar | listar | desfazer | refazer | sair')
    tarefa = input('Escola um comando: ')
    
    if tarefa == 'cadastrar':
        add_item = input('Digite uma tarefa? ')
        cadastrar(add_item, tarefas)
        salvar(tarefas, PATH_ROUTE)
        listar(tarefas)
    
    elif tarefa == 'listar':
        listar(tarefas)
    
    elif tarefa == 'desfazer':
        desfazer(tarefas, desfazer_tarefas)
        listar(tarefas)
        salvar(tarefas, PATH_ROUTE)

    elif tarefa == 'refazer':
        refazer(tarefas, desfazer_tarefas)
        listar(tarefas)
        salvar(tarefas, PATH_ROUTE)

    elif tarefa == 'sair':
        print('Saindo...')
        break
    else:
        print('comando inválido!')
