# Abstração (pilar do POO)
'''NotImplementedError -> Significa que você está usando uma superclasse 
que não era para ser usada.

Mixin -> Quando inserimos na classe, estamos dizendo aos demais devs que
essa classe é para add funcionalidades na sua herança múltipla que podem
NÃO ser dessa familia, como no exp abaixo (log)

RELEMBRE: 
'Se estamos uma Classe, estamos criando nosso próprio tipo'
'_log' -> (underscore) estamos dizendo que é um método para uso interno (protegido)

Extra: Template Method Patterns

O Template Method é um padrão de projeto comportamental em Python que 
permite definir o esqueleto de um algoritmo em uma classe base e 
permitir que as subclasses substituam as etapas sem alterar a estrutura geral do algoritmo.

Em resumo:

O Template Method encapsula o algoritmo em um método abstrato na classe base.
As classes concretas herdam dessa classe base e implementam os passos específicos do algoritmo.
O algoritmo em si permanece inalterado, mas os detalhes de implementação podem variar nas subclasses.

Vídeo extra (manipulação de path c/ pathlib): https://www.youtube.com/watch?v=T17BTNKBeJY
'''

# pathlib - modo profissional de manipular path
from pathlib import Path

# pegar o caminho absoluto
LOG_FILE = Path(__file__).parent / 'log.txt'


#superclass (abstração)
class Log:
    
    # todas subclasses heraram os methods
    
    def _log(self, msg): #assinatura do método
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        self._log(f'Success: {msg}')
    
#OBS: As demais subclasses precisam definir o método _log

#subclass(herança)
class LogFileMixin(Log):
    
    def _log(self, msg):

        msg_formatada = f'{msg} ({self.__class__.__name__})'

        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatada)
            file.write('\r\n')

        
        print(msg)

class LogPrintMixin(Log):
    
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Error')
    lp.log_success('Sucesso')

    lf = LogFileMixin()
    lf.log_error('Error')
    lf.log_success('Sucesso')
