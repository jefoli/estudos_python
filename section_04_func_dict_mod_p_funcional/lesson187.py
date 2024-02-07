# 187. with open (context manager) e métodos úteis do TextIOWrapper
'''
Criando arquivos com Python + Context Manager with
# Usamos a função 'open' para abrir
# um arquivo em Python (ele pode ou não existir)

Métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)


Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

OBS(1): SEMPRE que abrir um arquivo (open) temos que fechar(close)

OBS(2): Precisamos tratar a quebra de linha no arquivo com \r\n ...
    - Dessa forma, ele manipula o cursor do "Python" no arq. e não da IDE
    - Não é possível escrever + ler o arquivo sem utilizar o sinal de +

'''


path_arq = 'lesson187.txt'

# escrever no arquivo:
with open(path_arq, 'w') as arquivo:
    # escrever uma linha no arquivo:
    arquivo.write('Linha 1\r\n')
    arquivo.write('Linha 2')


#ler arquivo:
with open(path_arq, 'r') as arquivo:
    # escrever no arquivo:
    print(arquivo.read())


# WRITE + READ arquivo utilizando sinal de +:
with open(path_arq, '+w') as arquivo:
    # escrever no arquivo:
    arquivo.write('linha 3 (write+read)\r\n')

    #escreve várias linhas de uma vez:
    arquivo.writelines(('linha 4\n', 'linha 5\n'))

    # move o cursor do arquivo:
    arquivo.seek(0, 0) # volta para o topo do arquivo!

    # read() - faz a leitura do arquivo inteiro
    print(arquivo.read())
    
    arquivo.seek(0, 0) # volta para o topo do arquivo!
    
    # readline() - lê o arquivo linha por linha:
    print(arquivo.readline(), end='') #para remover o espaço
    print(arquivo.readline().strip()) #para remover o espaço do começo e do fim

    # readlines()
    for linha in arquivo.readlines():
        print(linha.strip())