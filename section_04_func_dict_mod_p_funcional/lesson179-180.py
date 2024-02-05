# 179-180 Funções recursivas, recursividade e Stack Overflow
'''
- interessante para programação funcional!

- Funções recursivas são aquelas que podem se chamar de volta.

- úteis para dividir problemas em partes menores.

- O corpo da func será salva na call stack a cada iteração!

Toda func recursiva deve ter:
    - Um problema que possa ser didivo em partes menores
    - Um caso recursivo que resolve o pequeno problema
    - Um caso base que para a recursão / retornar o valor

    - Exp: Fatorial - n! (5!) = 5 * 4 * 3 * 2 * 1 = 120

Stack Overflow = Quando excede o numero de recursões na call stack.

'''


def recursiva(inicio = 0, fim = 10):
    #Caso base/segurança:
    if inicio >= fim:
        return fim

    print(inicio, fim) # temos uma iteração dentro!
    
    # Caso recursivo
    # contar até o fim
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva()) # retorna o fim!


def factorial(n):
    
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))