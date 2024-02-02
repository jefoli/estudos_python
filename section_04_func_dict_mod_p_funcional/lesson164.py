# 164. Variáveis livres(free vars) + nonlocal (locals, globals)
'''
locals() - Retorna um dicionário contendo as variáveis locais do escopo atual.

var.__code__.co_frevars - Retorna as vars livres da função

print(globals()) -> Retorna todas variaveis globais definidas que podemos acessar.

nonlocal

'''
#print(globals())


def fora(x):
    a = x # var livre, pois não está definida no escopo da func 'dentro'
    
    def dentro():
        #print(locals())
        #print(dentro.__code__.co_freevars)
    
        return a
    return dentro

dentro = fora(10)

print(dentro())



def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        
        #UnboundLocalError:
        #valor_final += valor_a_concatenar #(gera erro), pois essa var não é desse escopo!
        
        # P para corrigir isso (nonlocal)
        nonlocal valor_final
        valor_final += valor_a_concatenar

        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
