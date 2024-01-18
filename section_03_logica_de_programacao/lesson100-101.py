# 100-101. Gerar o segundo dígito de um CPF com Python
"""
Calculo do segundo dígito do CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores por uma contagem regressiva começando de 11.

Ex.:  746.824.890-70 (7468248907)
    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
    77 40 54 64 14 24 40 36  0 14

Somar todos os resultados: 77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

R: O segundo dígito do CPF é 0
"""

cpf = '746.824.890-7'
cpf_limpo = cpf.replace('.','').replace('-','')

acumulador = 0
contador = 11

for i, digito in enumerate(cpf_limpo):
    acumulador += contador * int(digito)
    contador -= 1

calc_digito_2 = (acumulador * 10) % 11

if calc_digito_2 > 9:
    calc_digito_2 = 0
    print(f'Segundo dígito do CPF:{calc_digito_2}')
    cpf += str(calc_digito_2)
else:
    print(f'Segundo dígito do CPF: {calc_digito_2}')
    cpf += str(calc_digito_2)

print(cpf)

#Sugestão de resposta:
'''
cpf = '7468248907'

nove_digitos = cpf[:9]

dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_2)

'''


