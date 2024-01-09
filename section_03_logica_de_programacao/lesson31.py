#31. Uma introdução às f-strings (formatação de strings)

#breve introdução sobre f-strings:
# serve para formatar vars
# simbolo -> f   
# quando colocamos o f, podemos utilizar dentro dele 

#temos que usar f  + {}
#line_one = f'{nome} tem {altura} '


# tambem podemos formatar as casas decimais -> utilizar f + {} + :

#exp:
#line_one = f'{nome} tem {altura:.2f} '

# 2f = duas casas decimais
# podemos utilizar para fazer a conversão do ponto em virgula -> ,.2f

name = 'Luiz Otávio'
weight = 95
height = 1.80

imc = weight / height ** 2

#sem f-string:
print(name, ' tem', height)
print('pesa', weight,', e seu IMC é de', imc)

# com f-string:

line_one = f'{name} tem {height} de altura'

# com f-string + : .f (contador de casas decimais)
line_two = f'pesa {weight} e seu IMC é de {imc:.2f}'

print(line_two)


