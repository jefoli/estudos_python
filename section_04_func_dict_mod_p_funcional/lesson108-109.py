#108-109. Escopo de funções e módulos em Python + global
'''
Escopo -> Termo utilizado para definir a área em que uma variável pode ser acessada.

Tipos de escopo:

Escopo global -> Escopo global vale por toda sua aplicação, qualquer parte dela em execução tem acesso às variáveis de escopo global.

Escopo local -> Significa que a variável tem abrangência limitada. O mais comum é ser função, então ela só é visível dentro daquela função e não se confunde com outras partes do código.

OBS(1): Podemos utilizar/ manipular uma var do escopo global em um escopo local, porém é uma MÁ-PRÁTICA. Para isso, podemos utilizar a palavra -> global.

CALL STACK (pilha de chamadas):

- A pilha de chamadas (call stack) é um mecanismo do interpretador de uma linguagem que organiza o funcionamento do script quando são chamadas muitas funções, qual função está sendo executada no momento, e quais serão chamadas dentro de alguma função, etc.

- Em Python, a pilha de chamadas é implementada como uma lista. Quando uma função é chamada, o interpretador adiciona um novo elemento à lista, que contém informações sobre a função chamada, como o nome da função, os argumentos passados para ela e a linha do código em que a função foi chamada. Quando a função retorna, o interpretador remove o elemento da lista e continua a execução do script a partir do ponto em que a função foi chamada.

'''

x = 1 # escopo global

var_global = 1

def escopo():
    
    x = 10 # nova var dentro do escopo da func

    global var_global #OBS(1)
    var_global = 2000

    # escopo local:
    def outra_funcao():
        y = 2 # escopo local
        x = 20

        global var_global #OBS(1)
        var_global = 5000

        print(y, x)

    outra_funcao() #executamos a função interna
    
    print(x)

print(x)
escopo()
print(x)
print(var_global)
