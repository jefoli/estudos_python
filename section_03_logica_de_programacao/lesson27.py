#Class 27 (twenty-seven)
#Concatenação (+) e repetição (*) com operadores aritméticos
#além de somar, o sinal de + faz a concatenação -> ou seja, junta os valores!


#Concatenação
#se for só string, ele irá juntar o nome
concatenation = 'a' + 'b' +'c'
print(concatenation)

#OBS - se houver mistura de tipos o python não saberá interpretar e retornará um erro
# exp de erro -> a1 = 'a' + 3 + 'b' (há um number dentro da string)

#Evitar o exp acima, podemos usar uma coerção de tipo:
exp_with_coercion = 'texto' + str(2) + 'texto2'
print(exp_with_coercion)


#sinal de multiplicação pode fazer a repetição
#nesse caso temos que usar uma str e number
ten_x_a = 'A' * 10
print(ten_x_a)