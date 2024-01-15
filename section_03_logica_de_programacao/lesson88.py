# 88. Tipo tuple (tuplas) - Tuplas são uma lista imutável

# Formas de criar uma tupla:

# 1 forma - não envolver os valores:
carros = 'Ferrari', 'Mustang','Maserati'

#2 forma - envolver entre parenteses (mais específicos):
carros_2 = ('Ferrari', 'Mustang','Maserati')
print(carros_2)

#3 forma - converter uma lista em uma tupla:
carros_3 = ['Ferrari', 'Mustang','Maserati']
print(carros_3, type(carros_3))
conversao = tuple(carros_3)
print(conversao, type(conversao))