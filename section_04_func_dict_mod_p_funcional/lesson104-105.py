# 104-105. Introdução às funções Python - def define uma função
'''
# Documentação oficial: https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions

Funções são trechos de códigos usados para replicar determinada ação ao longo do código.
Uma função pode receber parâmetros (argumentos) e retorna um valor específico.
Obs: Por padrão, as funções em Python retorna None (= não valor).

Parâmetro -> variáveis definidas na função (a, b ,c)

A palavra reservada def inicia a definição de uma função. Ela deve ser seguida do nome da função e da lista de parâmetros formais entre parênteses. 

Os comandos que formam o corpo da função começam na linha seguinte e devem ser indentados.

'''
def imprimir(a, b, c):
    print(a,b,c)

imprimir('a', 1, 2) # passamos argumentos(valores) para executar a função

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Cleber Fernandes')

#Podemos passar um valor padrão para variaveis definidasa na func:
def cumprimento(saudacoes = 'Olá'):
    print(saudacoes)

cumprimento()
cumprimento('Bom dia')