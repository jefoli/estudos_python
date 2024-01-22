# 116-118. Exercício com funções
#Criar funções que duplicam, triplicam e quadriplicam o numero recebido como parâmetro


#solução:
def calculadora(multiplicar, qtd_repeticoes):
    numero_recebido = multiplicar
    qtd_vezes = qtd_repeticoes
    resultado = numero_recebido * qtd_vezes
    return resultado

valor_enviado = calculadora(2, 4)
print(valor_enviado)


#solução (proposta de resposta):

def criar_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

duplicar_valores = criar_multiplicador(2)
print(duplicar_valores(2))

triplicar_valores = criar_multiplicador(3)
print(triplicar_valores(2))

quadriplicar_valores = criar_multiplicador(4)
print(quadriplicar_valores(2))