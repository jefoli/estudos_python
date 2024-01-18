# 103. Criando um gerador de CPFs com nosso algoritmo e Python
# Podemos utilizar o módulo random

import random

cpf_nove_digitos = ''

for i in range(9):
    cpf_nove_digitos += str(random.randint(0, 9))

resultado_primeiro_digito = 0
cont_regressivo_1 = 10

for digito in cpf_nove_digitos:
    calculador_1 = (cont_regressivo_1 * int(digito))
    resultado_primeiro_digito += calculador_1    
    cont_regressivo_1 -= 1

resultado_primeiro_digito = (resultado_primeiro_digito * 10) % 11

resultado_primeiro_digito = resultado_primeiro_digito if resultado_primeiro_digito <= 9 else 0

print(f'Primeiro dígito: {resultado_primeiro_digito}')

cpf_dez_digitos = cpf_nove_digitos + str(resultado_primeiro_digito)

resultado_segundo_digito = 0
cont_regressivo_2 = 11

for digito in cpf_dez_digitos:
    calculador_2 = (cont_regressivo_2 * int(digito))
    resultado_segundo_digito += calculador_2
    cont_regressivo_2 -= 1

resultado_segundo_digito = (resultado_segundo_digito * 10) % 11

resultado_segundo_digito = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0

print(f'Segundo dígito: {resultado_segundo_digito}')

cpf_gerado = f'{cpf_nove_digitos}{resultado_primeiro_digito}{resultado_segundo_digito}'

print(cpf_gerado)