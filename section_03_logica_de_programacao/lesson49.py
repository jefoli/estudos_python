''' 49. Introdução ao try e except para capturar erros (exceptions)

try:
    ...
    # se ocorrer um erro dentro try, irá pula para except 
except:
    pass


# Try (tentar) -> tenta executar o código (caso ocorra qualquer erro, você captura o erro)

# Except -> Ocorreu um erro ao tentar executar o código

# levantar uma exceção = Mostrar um erro na tela (ValueError)

# .isdigit -> checa se o usuário digitou apenas números - se digitar valor com ponto irá retornar um erro.

'''

numero_str = input('Vou dobrar o número que você digitar: ')
# fail fast -> digitar uma letra ao invés de números para cair no except

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
    print('Você caiu no try except')
