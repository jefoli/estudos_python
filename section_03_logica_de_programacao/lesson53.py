# 53. Flags, is, is not e None
'''
Flag (bandeira) - Marcar no código para ver sua execução passou naquele local.

None = Não valor

IS e is NOT = é ou não é (tipo, valor, identidade)

Ideal para Módulos: Podemos utilizar essa estratégia quando importamos algum módulo e queremos saber se está retornando valor.

'''

condicao = False # ou True
flag_passou_no_if = None # ou False

if condicao:
    print('faça algo')
    flag_passou_no_if = True #flag
else:
    print('não faça algo')

print(flag_passou_no_if, flag_passou_no_if is None) # se o valor é None

print(flag_passou_no_if, flag_passou_no_if is not None) # se o valor não for None