# 167. Decoradores com parâmetros
'''
func decoradora = fábrica de funções

'''
#factory_dec = p/ pegar os params do decorador
def factory_decorators(a=None,b=None,c=None):
    
    #factory_function = O próprio decorador(tem que receber uma função!)
    def factory_function(func):
        print('Factory decorator 1')

        #inner substitui a função real(no exp=soma)
        def inner_func(*args, **kwargs):
            print('Params of decorator, ', a, b, c)
            result = func(*args, **kwargs)
            return result
        return inner_func

    return factory_function

#execução de baixo para cima
@factory_decorators(30,10,80) #segunda a ser executada
@factory_decorators(1,2,3) #primeiro a ser executado
def soma(x, y):
    return x + y


decorator = factory_decorators()
sum_numbers = decorator(lambda x, y : x + y)
#ou fazer direto:
ten_plus_five = factory_decorators(1,2,3)(lambda x, y : x + y)

print(sum_numbers(10,20))
print(ten_plus_five(10,20))
