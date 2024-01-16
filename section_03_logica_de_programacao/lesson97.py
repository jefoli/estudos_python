# 97. Operação ternária com Python (if e else de uma linha)
'''
Operação ternária (conndicional de uma linha)

<valor> if <condição> else <outro_valor>

'''
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9
novo_digito = 0 if digito > 9 else digito
# ou
#novo_digito = digito if digito <= else 0
print(novo_digito)

#não recomendável por conta da complexidade:
print('Valor' if False else 'Outro valor' if False else 'Fim')