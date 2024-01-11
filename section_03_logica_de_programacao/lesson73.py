# 73. range + for para usar intervalos de números
# range - range(start, stop, step)
#Obs: A função range não depende nada do FOR

numbers = range(10) # se colocarmos apenas um número fica igual = range(0, 10)
numbers_2 = range(5,10) # range com start + stop
numbers_3 = range(5, 10, 2) # range(start, stop, step)
print(numbers)
print(numbers_2)
print(numbers_3)


for number in numbers:
    print(number)

print('--' * 10)

#negative numbers
exp_1 = range(0, -10, -1)

for i in exp_1:
    print(i)