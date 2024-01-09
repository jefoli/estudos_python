''' 41. Operador Lógico "or"

OR - Qualquer uma das condições forem verdadeiras, toda expressão será True

Serão considerados falsy (0, 0.0 '' False)

Tipo NONE é usado para representar um NÃO valor

'''
entrada = input('[E]ntrar [S]sair: ')

senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha_permitida):
    print('entrar')
else:
    print('sair')

# AVALIAÇÃO CURTO-CIRCUITO (retorna o primeiro valor verdadeiro)
#podemos jogar o valor em uma variavel
    
senha = input('senha: ') or 'Sem Senha'

print(senha)


