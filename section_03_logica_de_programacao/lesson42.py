# 42. Operador lógico "not"
# utilizado para inverter expressões (o que for verdadeiro vira false e vice-versa)
# not True = False
# not False = True

senha = input('Senha: ')

# string vazia é considerado falso, logo se não for preenchido fica como falso
if not senha:
    print('senha incorreta!')

print(not False) # true
print(not True) # false