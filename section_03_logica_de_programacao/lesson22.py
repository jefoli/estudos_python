#22. Coerção de tipos (convertendo um tipo para outro)

#conversão de tipos, coerção

# type convertion, typecasting, coercion

# É o ato de converter um tipo em outro

'''
Tipos imutáveis e primitivos:

- str
- int
- float
- bool(==)

'''
#isso ocorrem em linguagem dinâmica e forte(PY), pois ele reconhece o que está dentro:
print(1+1)
print("a"+"b") #concatena -> usa o polimorfismo

#caso não seja possivel interpretar, ele vai retornar um erro na tela:
# print('1' + 1) ERRO

#OBS: se fosse linguagem dinâmica e fraca (JS) ele converteria e juntaria -> print('1', 1)

#No entanto, podemos fazer a conversão do valor utilizando um tipo primitivo:

print(int('10'),type('10'))

"""
texto do vscode:
int([x]) -> integer int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments are given. 
If x is a number, return x.__int__(). 
For floating point numbers, this truncates towards zero.

"""

print(int('1') + 1)
print(float('1') + 1)

print(bool(' '))