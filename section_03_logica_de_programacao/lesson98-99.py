# 98-99. Exercício - Gerar o primeiro dígito de um CPF com Python
"""
Calculo do primeiro dígito do CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores 
por uma contagem regressiva começando de 10.

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados: 70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

Dica: O primeiro dígito do CPF é 7
"""

# Minha resposta:
cpf_cliente = '746.824.890'
cpf_limpo = cpf_cliente.replace('.','')

acumulador = 0
contador = 10

for _, digito in enumerate(cpf_limpo):
    acumulador += contador * int(digito)
    contador -= 1

multiplicador = acumulador * 10

resto_divisão = multiplicador % 11

if resto_divisão > 9:
    
    resto_divisão = 0
    print(f'Primeiro dígito do cpf:{resto_divisão}')
    cpf_cliente += f'-{str(resto_divisão)}'
else:
    print(f'Primeiro dígito do cpf:{resto_divisão}')
    cpf_cliente += f'-{str(resto_divisão)}'

print(cpf_cliente)


'''
Sugestão de resposta:

cpf = '746824890'

nove_digitos = cpf[:9]

contador_regresivo = 10

for digito in nove_digitos:
    resultado += int(digito) * contador_regresivo
    contador_regresivo -= 1

digito = (resultado * 10) % 11

digito = digito if digito <= 9 else 0

print(digito)

'''