# 92. Imprecisão dos números de ponto flutuante + round e decimal.Decimal

# Double-precision | floating-point | format IEEE 754

# https://docs.python.org/pt-br/3/tutorial/floatingpoint.html


num_1 = 0.1
num_2 = 0.7
num_3 = num_1 + num_2
print(num_3)

# maneiras de contornar essa imprecisão:

# 1 forma -> utilizar format (.f)
print(f'função format: {num_3:.2f}') # aqui ele vira uma str. 

# 2 forma -> utilizar a função ROUND
# OBS: a função round recebe 2 argumentos, sendo o primeiro o número que desejamos utilizar a função e o segundo arg. o número de casas decimais.

print(f'funçao round: {round(num_3, 2)}') # aqui permanece o type como float

# 3 forma -> utilizar uma função chamada DECIMAL 
# o ideal é utilizar quando precisamos utilizar precisamente o valor!
import decimal
number_1 = decimal.Decimal(0.1) 
number_2 = decimal.Decimal(0.7)
number_3 = number_1 + number_2
print(f'função decimal: {number_3}')