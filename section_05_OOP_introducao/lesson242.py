# 242. Context Manager com contextlib.contextmanager
'''
Outra forma de um context manager é utilizando um decorator contextmanager
'''
from contextlib import contextmanager

# criamos uma função (generator) decorada:
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo...')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
    
        # usamos yield para fazer uma função generator
        yield arquivo

    except Exception as e:
        print('Ocorreu um erro', e)
    
    finally:
        print('Fechando arquivo')
        arquivo.close()


with open('aula242.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123) # 123 p/gerar um erro
    print('With', arquivo)