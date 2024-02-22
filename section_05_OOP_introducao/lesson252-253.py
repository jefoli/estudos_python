# 252-253. DocStrings em funções e classes (Documentação)

# def soma(x, y):

# 1) documentação de func com type annotations:
def soma(x: int | float, y: int | float) -> int | float:
    ...


def soma(x: int | float, y: int | float) -> int | float:
    """
    Este módulo contém funções e exemplos de documentação de funções.
    
    2) forma:

    :param x: Número 1
    :type x: int or float
    :param y: Número 1
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y