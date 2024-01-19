# 110. Retorno de valores das funções (return)

# Obs: Return para execução do código, logo o que estiver abaixo do "return" não será executado.

def soma (x, y):
    if x > 10:
        return 3000
    return x + y

soma_1 = soma(2, 2)
soma_2 = soma(3, 5)

print(soma_1 + soma_2)