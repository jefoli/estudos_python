#33. Usando a função input para coletar dados do usuário

#função input -> serve para enviar uma mensagem para entrada de dados + receber dados se estiver em uma variavel -> receber o que digitarmos

#input('Qual o seu nome? ') #só emite a mensagem = escreval(portugol)

# agora armazena o valor digitado
name = input('What is your name?') #input

print(f'Your name is: {name}') #output

#podemos pegar o nome + valor de uma variável de maneira mais fácil -> {name=} e obter o seguinte retorno:

#var + = 
#output name= 'João'

print(f'Your name is {name=}') 

num_1 = input('insert a number: ')
num_2 = input('Insert a second number: ')

print(f'A soma dos números é: {num_1 + num_2}') # output -> 33 - why? a saiu 33, pois a entrada de dados(números digitados) foi no formato STR. Desse modo, ao invés de somar, ocorreu a concatenação!!!

#correção

#podemos fazer typecast:

#NÃO É ACONSELHÁVEL FAZER ISSO, POIS GERA TRANSTORNOS
# Motivo -> se a pessoa digitar um a (str), vai quebrar o programa
# Desse modo, precisamos checar e depois criar uma nova variável para fazer a conversão de tipo!!

var_typecast1 = int(input('digite a number: '))
var_typecast2 = int(input('digite second number: '))

print(f'A soma dos números é: {var_typecast1 + var_typecast2}')


