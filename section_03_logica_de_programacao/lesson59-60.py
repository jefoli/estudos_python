'''
#59-60. while e break - Estrutura de repetição

while - executa uma ação enquanto uma condição for verdadeira

Obs: tomar cuidado com Loop infinito (bloco de código executado infinitamente)

'''

status = True
while status:
    name = input("Qual o seu nome: ")
    print(f'seu nome é: {name}')
    # quebrar laço (break ou status = False)
    #status = False
    break


counter = 0
while counter <= 10:
    print(f'Counter = {counter}')
    counter += 1 #ou counter = counter + 1 


