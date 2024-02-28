# 103. Criando um gerador de CPFs com nosso algoritmo e Python
# Podemos utilizar o módulo random

import random

nine_digit_cpf = ''

for _ in range(9):
    nine_digit_cpf += str(random.randint(0, 9))

first_digit_result = 0
first_countdown = 10

for digit in nine_digit_cpf:
    first_cpf_num_calculator = (first_countdown * int(digit))
    first_digit_result += first_cpf_num_calculator    
    first_countdown -= 1

first_digit_result = (first_digit_result * 10) % 11

first_digit_result = first_digit_result if first_digit_result <= 9 else 0

print(f'Primeiro dígito: {first_digit_result}')

ten_digit_cpf = nine_digit_cpf + str(first_digit_result)

second_digit_result = 0
second_countdown = 11

for digit in ten_digit_cpf:
    second_cpf_num_calculator = (second_countdown * int(digit))
    second_digit_result += second_cpf_num_calculator
    second_countdown -= 1

second_digit_result = (second_digit_result * 10) % 11

second_digit_result = second_digit_result if second_digit_result <= 9 else 0

print(f'Segundo dígito: {second_digit_result}')

generate_cpf = f'{nine_digit_cpf}{first_digit_result}{second_digit_result}'

print(generate_cpf)