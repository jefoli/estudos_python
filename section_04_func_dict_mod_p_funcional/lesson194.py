# 194. Evitando uso de condicionais + Guard Clause
'''
Código com menos condidicionais e perto da margem é melhor,
pois tem menos riscos de bugs!

artigos sobre guard clause: 
    https://en.wikipedia.org/wiki/Guard_(computer_science)
    https://medium.com/lemon-code/guard-clauses-3bc0cd96a2d3
    https://medium.com/@niiicolai/design-pattern-guard-clause-c050a26dcf35
'''

# refatorando menu do exercício anterior para evitar if:

# 1) forma mais complexa de ler 
# adiar a execução da função com lambda para não dar erro no dict de comandos:
def listar(tarefas):
    print()
    for tarefa in tarefas:
        print(tarefa)
    print()

def sair(comando):
    comando = False
    return comando

tarefas = ['Casa', 'Carro']
control = True

while control:
    tarefa = input('digite uma tarefa ou comando: ')
    comandos = {
        # lambda está sendo retornada para evitar a execução da func
        'listar': lambda: listar(tarefas),
        'sair': lambda: sair(control),
    }
    comando = comandos.get(tarefa)() # precisa colocar ()
    control = comando
print()

# 2) forma match-case:
print('Match case: ')
while True:
    tarefa_2 = input('digite uma tarefa ou comando: ')

    match tarefa_2:
        case 'listar':
            listar(tarefas)