# 128-130. Métodos úteis do tipo set em Python (conjuntos)
'''
Sets conjuntos em python (tipo set)
Sets são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

formas de cria um set:
    1) set():
    2) {1, 2, 3}
        - Obs(1): É necessário colocar valores dentro de {}, caso contrário seja criado um dicionário! Para cria um set vázio -> var = {''}

Dicas:
    - Sets são eficientes para remover valores duplicados de iteráveis.
    - Seus valores serão sempre únicos, logo não haverá repetidos.
    - Não aceitam valores mutáveis.
    - Não possuem índex, logo não podemos acessar um valor pelo index
    - Não garantem a ordem das informações.
    - São iteráveis (for, in, not in)

Métodos úteis (mais utilizados):
    - add
    - update
    - discard (passar o valor p/ excluir, pois não há índice)
    - clear


Operadores úteis:
    | -> união | união (union) - Faz a união
    & -> intersecção & (intersection) - Itens presentes em ambos
    - -> diferença - Itens apenas no set da esqueda
    ^ -> diferença simétrica - Itens que não estão em ambos
'''
# add
s1 = set()
s1.add('Magnólia')
s1.add(2)

print(s1)

# update
s2 = s1.copy()
s2.update('Hi') # ele itera a string
s2.update(('Olá mundo', 2)) # tupla evita iteração do str
print(s2)

# discard
s2.remove('Magnólia')
print(s2)

# clear
s2.clear()
print(s2)

conjunto_1 = {1,2,3}
conjunto_2 = {2,3,4}

# union:
unir_sets = conjunto_1 | conjunto_2
print(unir_sets)

# intersecção:
interseccao_sets = conjunto_1 & conjunto_2
print(interseccao_sets)

# diferença (Apenas itens presentes no set da esquerda):
diferenca_sets = conjunto_1 - conjunto_2
print(diferenca_sets)

# diferença simétrica (itens NÃO estão presentes em ambos):
diferenca_simetrica_sets = conjunto_1 ^ conjunto_2
print(diferenca_simetrica_sets)


# Exemplo de uso dos sets (procurar valor dentro dele):
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print("Você encontrou a letra!")
        break

    print(letras)
