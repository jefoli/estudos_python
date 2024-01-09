
# aula 35. if, elif e else: entendendo o fluxo do interpretador em condicionais

#ELSE -> SERÁ SEMPRE A ÚLTIMA CONDIÇÃO A SER EXECUTADA!

# Quando encontrar a primeira condição verdadeira, o código irá finalizar

condicao = True

#if sozinho
if condicao:
    print('Este é o código do if')

print('fora do if')

condicao1 = False
condicao2 = False

#if-elif-else
if condicao1:
    print('Este é o código do if')
elif condicao2:
    print("elif")
else:
    print('Caiu no else')

