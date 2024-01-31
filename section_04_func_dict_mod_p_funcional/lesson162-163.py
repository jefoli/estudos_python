# 162. Exercício - Adiando execução de funções (generator e closure)

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def internal(y):
        return funcao (x, y)
    return internal


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_10 = criar_funcao(multiplica, 10)

print('Soma', soma_com_cinco(34))
print('Multiplicar:', multiplica_por_10(10))