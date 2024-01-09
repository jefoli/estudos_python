# 45. Formatação de strings com f-strings

'''
Formatação básica de strings

s - string
d - int 
f - float
.<n de dígitos>f (.2f)
x ou X - Hexadecimal

(Caractere)(><^)(quantidade)

> - esquerda
< - direita
^ - centro
= - Força o número aparecer antes dos zeros

Sinal - + ou -

Ex.: 0>-100, 1.f

conversation flags - !r !s !a
!r -> chama o médoto __repr__
!s -> chama o método __str__
!a -> chama o método __asc__

'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #coloca um pad (espaço)
print(f'{variavel:#<10}')
print(f'{variavel:#^10}')
print(f'{1000.333333:.2f}')
print(f'{1000.333333:+,.2f}') # sinal é só para mostrar se o valor é positivo ou negativo
print(f'{-1000.333333:-,.2f}') # sinal é só para mostrar se o valor é positivo ou negativo
print(f'{-1000.333333:0=+10,.1f}') #insere uma quantidade de 0
print(f'O hexadecimal de 1500 % {1500:08X}') # (x - minúsculo) (X - Maiúsculo)


print(f'{variavel!r}') # !r chama o método de dentro da string

