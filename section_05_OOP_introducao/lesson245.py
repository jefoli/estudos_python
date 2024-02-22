# 245. Método especial __call__
"""
método especial ___call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma classe 'callable'.

Ele faz a instância/objeto da classe ser executável.
"""

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwgs):
        print('Chamando', args, self.phone)

call_1 = CallMe('2222222222')
call_1()
call_1('Jeferson') # instância executa a ação