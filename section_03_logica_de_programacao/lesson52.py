# 52. id - A identidade do valor que está na memória
'''
id = identidade

# para você verificar em que local da memória está armazenado a variável, basta utilizar id(var)

#OBS: Dependendo da ocasião, o interpretador do python pode apontar o mesmo endereço de memória a outra variável se o seu valor for o mesmo.
'''
primeira_variavel_armazenada = 'a'
print(id(primeira_variavel_armazenada))

segunda_variavel_armazenada = 'b'
print(id(segunda_variavel_armazenada))

print(15 * '-')

#OBS: Dependendo da ocasião, o interpretador do python pode apontar o mesmo endereço de memória a outra variável se o seu valor for o mesmo.

var_mesmo_local_1 = 1
var_mesmo_local_2 = 1

print(id(var_mesmo_local_1))
print(id(var_mesmo_local_2))