# 113. Exercícios com funções + args
'''
1) Crie uma função que multiplica todos os argumentos NÃO nomeados recebidos;
Retorne o total para uma variavel e mostre o valor da variável.

2) Crie uma função para informar se o número é par ou ímpar;
Retorne a informação "Par" ou "ímpar"

'''
# exercício 1:
def multiplicar(*args):
    total = 1
    
    for valor in args:   
        total *= valor
    
    return total

multiplicacao = multiplicar(3, 4, 6) 
print(multiplicacao)

# exercício 2:
def par_impar(valor):

    check_par_impar = "Par" if valor % 2 == 0 else "Ímpar"
    
    return check_par_impar

retorno_par_impar = par_impar(4)
print(retorno_par_impar)

