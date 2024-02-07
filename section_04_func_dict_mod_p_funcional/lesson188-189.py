# 188-189. Modos de abertura de arquivo e encoding com with open

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


# Temos que importar o módulo os
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

OBS: SEMPRE que abrir um arquivo (open) temos que fechar(close)

W x A

w - abre o doc, apaga tudo que está no arquivo e escreve novamente.

a - Não apaga nada do arquivo - Inicia na última linha do doc

Mais utilizado: R, W, A

OBS: Atenção para tabela de caracteres utilizada UNICODE (especialmente o windows)
    - padrão: UTF-8
    - Se não identificarmos para o py, ele vai utilizar do sistema!
    - p/ resolver -> usar open(, encoding='utf-8')

'''
import os 

arq_example = 'lesson188.txt'

# W
with open(arq_example, '+w') as arquivo:
    arquivo.write('Linha 1\r\n')

# A
with open(arq_example, '+a') as arquivo:
    arquivo.write('Linha 100\r\n')

# B - abre o arquivo em modo binário
#with open(arq_example, 'b') as arquivo_3:
#    ...


# (encoding): para o windows salvar em UTF-8
with open(arq_example, '+w', encoding='utf-8') as arq_4:
    arq_4.write('Atenção\r\n')
    arq_4.write('arquivo com encoding UTF-8 \r\n')


# módulo os.rename(renomeia o arquivo)
os.rename(arq_example, 'aula188-copy.txt')


# Módulo os.remove ou unlink - apagar arquivo
os.remove(arq_example)

os.unlink(arq_example)
