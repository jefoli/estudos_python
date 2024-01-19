# 107. Valores padrão para parâmetros em funções Python + NoneType e None
'''
Ao definir uma função, os parâmetros podem ser valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado

# Obs: se colocarmos 0 (zero) em algum parâmetro, pode ocorrer erro, pois retorna Falsy!
# O ideal é colocar o valor padrão como None!

OBS(1): Toda vez que nomearmos um parâmetro, obrigatoriamente devemos nomear os próximos!


'''
def somar(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


somar(2, 4)
somar(2, 5, 0)
somar(x=3, y=39, z=73)