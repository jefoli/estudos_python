# 166. Decoradores em Python (@syntax_sugar)
'''
Decoradores são "Syntax Sugar" 
Funções decoradoras em Python são funções que modificam ou aprimoram o comportamento de outras funções ou métodos, sem alterar o código interno delas. 

Elas são usadas com a sintaxe @decorador acima da definição da função que será decorada.

Obs: aparamente o python troca o nome da função decorada para o nome da função interna do decorator...
'''

def create_function_decorator(func):
    #closure:
    def internal_function(*args, **kwargs):
        for arg in args:
            check_str(arg)
        result = func(*args, **kwargs)
        print(f'Seu resultado foi {result}')
        print('Função decorada!')
        return result
    return internal_function


@create_function_decorator #sugar - queremos use essa função na função invert_string

def invert_string(string):
    #print(f'{invert_string.__name__}')
    return string[::-1]


def check_str(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


txt_inverted = invert_string('Jeferson')
print(txt_inverted)