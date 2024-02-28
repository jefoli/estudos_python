# 93. (split, join e strip) - métodos muito úteis da str
""" 
split - tem a função de dividir uma string
    - .split() -> Vázio - separa as palavras nos espaços em branco!
    - Podemos passar parâmetros dentro do split.

var.strip() - tem a função de cortar os espaços do começo e do fim da string
var.rstrip() - tem a função de cortar os espaços da direita
var.lstrip() - tem a função de cortar os espaços da esquerda

join - tem a função de unir uma string
    - primeiro tem que criar uma string vazia (var = '') onde '' é utilizado para separação dos itens do iterável. 
    - Em seguida, chama .join() e passa o parâmetro dentro.

Obs: Utilizando expressões regulares (Regex) ou list comprehension, a separação fica refinada.
"""

frase = 'Olha só que    , coisa interessante     '
lista_palavras = frase.split(',')


# podemos utilizar for na lista para altera-la:
lista_frases_fixed = [] # geramos nova lista, para não alterarmos os valores da frase original
for i, frase in enumerate(lista_palavras):
    lista_frases_fixed.append(lista_palavras[i].strip())

print(lista_palavras)
print(lista_frases_fixed)

# Método join() - é um método da str

frases_unidas = '-'.join(lista_frases_fixed) # nessa string que falamos qual é o separador que vamos utilizar (colocar dentro de '' [aspas] o que desejamos inserir)

print(frases_unidas) # inseriu traço onde as frases eram separadas por vírgula