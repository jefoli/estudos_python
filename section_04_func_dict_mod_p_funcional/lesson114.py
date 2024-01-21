# 114. Higher Order Functions - Funções de primeira classe
'''
Em Python, funções são consideradas de primeira classe (first-class functions), 
o que significa que elas podem ser tratadas como qualquer outra variável, como inteiros, strings, listas, etc. 
Isso proporciona flexibilidade e poder ao lidar com funções. 

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções


'''


def mensagem(msg, nome):
    return f'{msg}, {nome}!'

def executa(func, *args):
    return func(*args)


valor = executa(mensagem, "Bom dia!", "Luiz Fernando")

print(valor)
