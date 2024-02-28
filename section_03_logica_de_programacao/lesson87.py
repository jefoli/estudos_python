# 87. Introdução ao empacotamento e desempacotamento
"""
OBS(1): _ (CONVENÇÃO) quando não vamos mais utilizar um valor de uma lista, 
inserimos _ (underline) para indicar que há uma var naquele local, porém não será utilizada.
"""

nomes = ['Maria', 'Helena', 'Fernando'] # desempacotar - extrair os valores e inserir em variaveis
nome1, nome2, nome3 = nomes
# mesma coisa que o exemplo acima:
nome1, nome2, nome3 = ['Maria', 'Helena', 'Fernando']
print(nome2)

# se tentarmos extrarir somente um valor, o Python irá retornar uma mensagem de erro 'too many, values to unpack).

# Para evitarmos isso, é necessário desempacotar, extrair o valor que deseja, e empacotar novamente! 

# Para evitarmos o erro, o correto é criarmos uma var e utilizar (*) asterisco.
name1, *rest = ['Camões', 'Machado', 'Quincas']
print(name1)
print(rest) # lista com o restante dos valores!


# OBS(1)
name1, *_ = ['Camões', 'Machado', 'Quincas']
print(name1)


# Se quisermos pegar o segundo valor, basta pular ele.
_, name2, *_ = ['Lucas', 'Ronaldo', 'Moacyr']
print(name2)