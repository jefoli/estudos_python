# 134. Funções lambda complexas (para entendimento)
# OBS: Se a função lambda ficar muito complexa para entender, a melhor prática será criar uma func padrão!

# função que executa outra func
def executa(funcao, *args):
    return funcao(*args)

# função padrão
def soma(x, y):
    return x + y
print(executa(soma, 2, 5))


# Mesma função em lambda:
print(executa(lambda x, y: x + y, 2, 5))
#ppodemos usar args:
print(executa(lambda *args: sum(args), 1,2,3,4,5,6,5))


# função que retorna outra func
def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# mesma func em lambda, porém + complexo (não recomendado)
duplica = executa(
    lambda m : lambda n : n * m, 2
)
print(duplica(2))

