# 186. Criando arquivos com Python + Context Manager with

'''
Criando arquivos com Python + Context Manager with
# Usamos a função 'open' para abrir
# um arquivo em Python (ele pode ou não existir)

Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final do arquivo), b (binário)
# t (modo texto), + (habilta leitura e escrita)
# Context manager - with (abre e fecha)

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


OBS: SEMPRE que abrir um arquivo (open) temos que fechar(close)

'''

#criamos o caminho de um arquivo:
path_arq = 'arq186.txt' #cria uma pasta na pasta que estamos

# no windows temos que trocar uma barra \ para \\, podemos colocar um r'c:..\\' caso dê erro no exemplo abaixo
full_path_arq = 'C:\\Users\\...\\...'

# Criar + abrir um arquivo:

arquivo = open(path_arq, 'w') #criar arquivo
arquivo.close() #sempre fechar o arquivo

# WITH -> Ele sempre vai abrir e fechar o arquivo sem a necessidade de colocar .close()
with open(path_arq, 'w') as arquivo:
    print('Olá mundo')