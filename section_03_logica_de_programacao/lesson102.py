# 102. Exercício - Gerar 2 últimos números + validação de CPF (Código procedural)

import re # (Opcional) - Temos que importar o módulo p/ utilizar o regex
import sys # (opcional) - módulo para encerramos a execução do código

cpf_usuario = input('Digite seu CPF: ')

#formas de limpar o CPF:

# 1 forma(métodos)
# limpar_cpf = cpf_usuario.replace('.','').replace('-','').strip()

# 2 forma (Regex) - re.sub() - Remove todos caracteres que não for número:
cpf_usuario_tratado = re.sub(r'[^0-9]','', cpf_usuario)
#print(limpar_cpf)

entrada_qtd_char = False if len(cpf_usuario_tratado) == 11 else True

entrada_valor_seq = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)

print(entrada_qtd_char, entrada_valor_seq)
if entrada_qtd_char or entrada_valor_seq:
    print("Digite corretamente seu CPF!")
    sys.exit() # encerra o programa em caso de erro!

cpf_nove_digitos = cpf_usuario_tratado[:9]

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

# validação de CPF

if cpf_usuario_tratado == cpf_gerado:
    print(f'CPF válido!')
else:
    print('CPF Inválido')