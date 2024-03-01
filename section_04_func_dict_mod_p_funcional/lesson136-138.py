# 136-138. List comprehension em Python (mapeamento, filter)
"""
list comprehensions é uma forma rápida para criar lista a partir de iteráveis!

mapeamento - Gerar uma nova lista de uma lista existente, podendos transformar seus dados
e manter o mesmo tamanho/índice das listas 

filtro - determinar que algum elemento não incluído na lista se alguma condição não for verdadeira
    - Basicamente o filtro é um if que vem depois do for.

OBS: exemplos abaixos possuem if antes e depois do for, o que significa que
if antes do for = ternário e após o for = filtro (não recebe else)    

vídeo complementar: https://www.youtube.com/watch?v=1YbTDczvqco
"""
# estilizar visualização da saída dos dados:
import pprint
def imprimir(imprimir):
    pprint.pprint(imprimir, sort_dicts=False, width=40)


# criar lista de forma comum
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# criar lista com list comprehension:
# Precisa colocar a esquerda do for o que será incluído
lista_2 = [numero for numero in range(10)]
print(lista_2)

#podemos criar lógicas dentro:
lista_3 = [numero * 2 for numero in range(10)]
print(lista_3)


produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 20},
]

# mapeamento + novo dict
novos_produtos = [
    # novos dicionários:
    
    #{'nome': produto['nome'], 'preco':produto['preco']} for produto in produtos
    
    #aumentar preço antigo:
    #{**produto, 'preco': produto['preco'] * 1.05} for produto in produtos

    #aumentar preço antigo se for maior que 20
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
]

print(*novos_produtos, sep='\n')
imprimir(novos_produtos)

# Filtro em list comprehension
lista_4 = [n for n in range(10) if n < 5]
imprimir(lista_4)

novos_produtos_2 = [
    {**produto, 'preco': produto['preco'] * 2.00} 
    if produto['preco'] > 10 else {**produto}
    for produto in produtos if produto['preco'] >= 20
]

imprimir(novos_produtos_2)