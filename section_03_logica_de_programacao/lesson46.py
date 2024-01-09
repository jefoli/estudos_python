# 46. Fatiamento de strings e a função len

'''
Fatiamento de strings

012345678 (índice)
ola mundo
-987654321 (índices negativos - começa do -1)

Fatiamento [i:f:p] [::] (i - inicio | f - fim | p - passo)

FUNÇÃO LEN (conta caracteres das strings)

Obs.: a função len retorna a qtd de caracteres da string

Obs2.: índice final não é íncluido

print(variavel[::-1]) # PASSO NEGATIVO INVERTE A STRING

'''

variavel = 'ola mundo'
print(variavel[-4])

#Fatiamento utilizando i (inicio)
print(variavel[4:]) # omite o fim para ir até o final 

#Fatiamento utilizando f (final)
print(variavel[:5]) # omite o inicio

#Fatiamento utilizando i (inicio) e f (final)
print(variavel[4:7]) # omite o índice 7 (não é incluído)

#Fatiamento utilizando i (inicio) e f (final)
print(variavel[0:5]) # omite o índice 5 (não é incluído)

#FUNÇÃO LEN (conta caracteres das strings )

print(len(variavel[3]))
print(len(variavel)) # está contando os caracteres e não retornando os valores dos index


# p (passo) - quantidade de caracteres que irá pular
print(variavel[0:9:1]) # passo 1 (vai de um em um)
print(variavel[0:9:2]) # passo 2

print(variavel[::-1]) # PASSO NEGATIVO INVERTE A STRING
#OU
print(variavel[-1:-10:-1]) # PASSO NEGATIVO INVERTE A STRING