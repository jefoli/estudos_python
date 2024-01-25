# 144. dir, hasattr e getattr para checar métodos em Python

#dir - saber quais métodos estão disponíveis:

string = 'Luiz'
print(dir(string))

# hasattr - checa se um determinado objeto teterminado método dentro
if hasattr(string, 'upper'):
    print('Existe Upper!')
    print(string.upper())


# getattr

string_2 = 'Carlos'
metodo = 'upper' #lower, strip - que não tem params

if hasattr (string_2, metodo):
    print(getattr(string_2, metodo)())
else:
    print('Não existe o método')
    