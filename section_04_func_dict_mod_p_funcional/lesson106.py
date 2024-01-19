# 106. Argumentos nomeados e argumentos posicionais (não nomeados) em funções
'''
Argumentos nomeados - tem nome com sinal de igual 
argumento posicional/não nomeado - recebe apenas o argumento (valor)

parâmetro -> nome das variaveis dentro de uma função

OBS(1): Toda vez que nomearmos um argumento, obrigatoriamente devemos nomear os próximos!

'''

#definição de função
def soma(x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

soma(1, 2) # argumento posicional (depende da ordem dos argumentos)
soma(y=2, x=3) #argumento nomeados

def soma_2(x, y, z):
    print(x + y + z)

soma_2(1, y=3, z=5) # (OBS(1))