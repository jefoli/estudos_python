# 165. Funções decoradoras em geral (decorators)
'''
Decorar = Adicionar / Remover / Restringir / Alterar

Funções decoradoras são funções que decoram outras funções

Decoradores são usados para fazer o Py usar as funções decoradoras em outras funções

'''

#função decoradora:
def create_func_decorator(func):
    def internal_func(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'O seu resultado foi {result}')
        print(f'Agora função foi decorada!')
        return result
    return internal_func 


def invert_string(string):
    return string[::-1]

def is_string(arr):
    str_check = isinstance(arr, str)

    if not str_check:
        raise TypeError('Params deve ser uma string!')


check_params_str = create_func_decorator(invert_string)
invert = check_params_str('123')
print(invert)