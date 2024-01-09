''' 40. Operador Lógico "and"

Operadores lógicos and

AND - todas as condições precisam ser verdadeiras!

(Se qualquer valor for cinsiderado falso, a expressão inteira será avalianda naquele valor serã considerado falsy) -> 0 . 0.0 '' False

0 . 0.0 '' -> são considerados falsos apenas quando confrontados com bolean!

Também existe o tipo NONE que é usado para representar um não valor (valor não existe)!

'''

# exemplo

entrada = input('[E]ntrar [S]sair: ')

senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')

print(True and True)

# Avaliação de curto circuito -> Retorna o valor False
print(True and False and True)

print(True and 0 and True) #false -> retorna o valor da condição!