# Exercício de programação com if e comparação

# utilizar if + operador de comparaçãoS

primeiro_valor = input('digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'primeiro_valor= {primeiro_valor} é maior que o segundo')
else:
    print(f'segundo_valor= {segundo_valor} é maior que o primeiro')

# segunda forma:
    
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')