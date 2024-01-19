# 111-112 *args para quantidade de argumentos não nomeados variáveis
'''
* - *args (empacotamento e desempacotamento) - são tudo que passarmos para como argumento não nomeado para função.

*args retorna uma tupla empacotada, porém podemos converter.
'''

# Desempacotador:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def somar_1(*args):
    print(args, type(args))

somar_1(1, 2, 3, 4)

def somar_2(*args):
    total = 0
    for i in args:
        total += i
    return total

calculo = somar_2(10, 20, 30, 40, 50)
print(calculo)

calculo_2 = somar_2(100, 99, 33, 482, 1)
print(calculo_2)


# quando temos um valor empacotado e passamos a função, por padrão vai retornar um erro.
# para evitar que isso ocorra, basta desempacotar a var desejada e passar como argumento.

exemplo_empacotado = 1,3,4,6,7,8,9,200

def somar_3(*args):
    total_soma = 0
    for i in args:
        total_soma += i
    return total_soma

somar_desempacotado = somar_3(*exemplo_empacotado)
print(somar_desempacotado)

#Exp com erro:
#sem_desempacotar = somar_3(exemplo_empacotado)
#print(sem_desempacotar)