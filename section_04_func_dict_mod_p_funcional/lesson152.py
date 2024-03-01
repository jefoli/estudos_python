# 152. raise - lançando exceções (erros)
"""
A instrução raise é usada para lançar (ou gerar) uma exceção deliberadamente em 
um ponto específico do código.

Erro é utilizado quando não temos o que fazer algo.

podemos criar um erro com -> raise (tem a função de relançar a exceção)

Diferença entre try-except e raise:
- O raise é usado para criar e lançar exceções explicitamente.
- O try-except é usado para capturar e tratar exceções que podem ocorrer durante 
a execução do código.
"""

print(123)
#raise ValueError('Deu erro!') #Lançamos um erro no código!
#print(456)


# Cria nosso próprio erro(alteraos mensagem de retorno):
def dividir(n, d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return n / d
#print(dividir(8, 0))

def nao_aceita_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0')
    return True

def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'"{n}" deve ser int ou float.'
                        f'"{tipo_n.__name__}" enviado')

def divisao(n, d):
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    nao_aceita_zero(n)
    nao_aceita_zero(d)
    return n / d

print(divisao(8, '0'))

