#AULA 26 - Introdução aos operadores aritméticos (matemática)

#addition/plus -> somar

# sub/subtraction/minus -> subtração

# mult/multiplication -> multiplicação

# Division -> divisão

#Module -> módulo (resto da divisão)

#exponentiation -> exponenciação

#sum / add

plus = 10 + 10
print(plus)

#obs -> if sum int number with float number, the output is a flot!
# example:
plus_with_float = 10 + 19.5
print('the sum is: ', plus_with_float, ', Your type is: ', type(plus_with_float)) 

#subtração
subtraction = 10-5
print(subtraction)

#multiplicação
multiplication = 10 * 5
print(multiplication)

#divisão
#Always return float number!

division =  10 / 2.2
print(division)

#divisão inteira -> trunca o numero?
# não retorna as casas decimais
# não retorna o número depois do ponto 
integer_division = 10 // 2.2
print(integer_division)

#Example -> When division 10 with 3, it's return a large num after common
#If we use interger_division, don't show de number after common(virgula p/ português) or dot(ponto-inglês)

division_with_numbers_after = 10 / 3
division_without_number_after = 10 // 3

print(division_with_numbers_after)
print(division_without_number_after)

#exponentiation (exponenciação)
#eleva o número

exponentiation = 2 ** 10
print('exponenciação', exponentiation)


#module (módulo)
# resto da divisão (é o número que sobra da divisão)
# exp -> 3 / 2 = 1 (resto 1)

module = 25 % 5
print('Modulo', module)

#para saber se o número é múltiplo de 8

print(10 % 8 == 0) # se restar 0, é múltiplo de 8

#par ou impar
print(10 % 2 == 0) #par

#expressão condicional para ver se é par ou impar!!!
#expression condition to test if var is even or odd!
par_ou_impar = 39

if(par_ou_impar % 2 == 0):
  print('par')
else:
  print('impar')
