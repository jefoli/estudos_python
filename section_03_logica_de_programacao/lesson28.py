#28. Precedência entre os operadores aritméticos
# Na precedência de valores - serão executados de dentro para fora -> Se houver mais de um parenteses, será executado primeiramente o mais interno

#order:

# 1 -> (n + n)
# 2 -> ** (exponenciação)
# 3 -> * - / - // - %
# 4 - + - 

operation_one = 1 + 1 ** 5 + 5 
print(operation_one) # result -> 7

operation_two = 2 * (10 * (3 * (30 - 10))) # 1200
print(operation_two)

#temos a possibilidade de trocar o valor de uma variável durante a rodagem do programa, porém NÃO é aconselhável!

change_value = 10
print(change_value)
change_value = "Value Changed!"

print(change_value)