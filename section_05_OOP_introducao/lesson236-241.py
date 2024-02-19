# 240-241. Context Manager com classes - Criando e Usando gerenciadores de contexto
# Exceptions em context manager com classes

'''
Você pode implementar seus próprios protocolos apenas
implementando os dunder methods o que o Python vai usar.

Isso é chamado de "duck typing". 
Um conceito relacionado com tipagem dinâmica onde o Python não está interessado
no tipo(int, str, class...), mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.

Para criar um context manager, os métos __enter__ e __exit__ devem ser implementados.

O método __exit__ receberá a classe de exceção, a exceção e o traceback.
Se retornar True, exceção no with será suprimida.

Outra forma de criar um context manager c/ decorator: contextlib.contextmanager

'''
# Exp que já funciona como um context manager:
#with open('aula236.txt', 'w') as file:
#    ...

#implementando um context manager para abrir arquivo:
class MyContextManager:
    
    def __init__(self, path_arq, mode):
        self.path_arq = path_arq
        self.mode = mode
        self._file = None
        #print('INIT')
    
    def __enter__(self):
        print('Abrindo arquivo...')
        self._file = open(self.path_arq, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo...')
        self._file.close()

        #obs: __exit__ nos fornece:
        print(class_exception) #classe da exceção
        print(exception_) #exceção em si
        print(traceback_) #traceback
        # dessa forma, podemos remontar/cria uma exceção

        #raise class_exception('Minha exceção')

        #remontar (é possível, mas não faz sentido):
        #raise class_exception(*exception_.args).with_traceback(traceback_)
        
        # exception_.add_note('Minha nota')
        
        return True # True significa (tratei a exceção)

with MyContextManager('aula236.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 1223) #colocamos 1223 para gerar uma exceção
    print('With', file)

''' 
OU
instancia = MyContextManager('aula236.txt', 'w')
with instancia as file:
#  print('WITH', file)
'''