# 246. Classes decoradoras (Decorator classes)
"""
A própria classe que decora o objeto

OBS: o decorador tem que ser c/ a primeira letra maiúscula: @Decorator
"""

from typing import Any


class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    # __call__ está fazendo que a instância seja tratada como uma função.
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(args, kwargs)
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Multiplicar
def soma(x, y):
    return x * y

dois_mais_dois = soma(2, 2) #  args e kwargs recebem os argumentos passados p/ func soma
print(dois_mais_dois)


class Dividir:
    def __init__(self, dividir):
        self._divisor = dividir

    def __call__(self, func):
        def decorator(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado *self._divisor
        return decorator

# @Dividir() -> c/ () muda o comportamento da classe, pois executa o __init__
@Dividir(2)
def somar(x, y):
    return x + y

fazer_soma = somar(2, 4)
print(fazer_soma)