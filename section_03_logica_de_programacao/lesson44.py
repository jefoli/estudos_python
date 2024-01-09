# 44. Interpolação de string com % em Python

'''
interpolação básica de strings (semelhantea format) - vem da linguagem C

%s - string

%d e %i - int

%f - float

x e X - Hexadecimall(ABCDEF0123456789)

'''

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco) # a interpolação estão dentro de ()
# %s p/ (nome) e %.f(preco)
print(variavel)

print(20 * '-')

print('O hexadecimal de %d é %04x' % (1500, 1500)) # (x - minúsculo) (X - Maiúsculo)