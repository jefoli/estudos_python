# 155. Como importar coisas do seu próprio módulo (ponto de vista do __main__)
'''
- SEMPRE o primeiro módulo executado no python chama-se __main__

- Podemos importar outros módulos inteiros ou parte do módulo
    Obs: Tomar cuidado para colocar nome de módulo igual aos que já existem

- O Python conhece a pasta onde o __main__ está sendo executado abaixo dele

- Por padrão o Python não reconhece módulos acma do __main__ (exp: arquivo de outra pasta(pacotes))

- Python conhece todos os módulos e pacotes presentes nos caminhos sys.path

-> __main__ é o ponto de entrada!
    - Só conhece os seus módulos irmãos.
    - para procurar outros módulos para trás, temos que manipular o sys.path()

'''

import lesson113
from lesson113 import multiplicar, multiplicacao
#print('Esse módulo se chama', __name__)

print('print', lesson113.multiplicar(5,3))

print(multiplicacao)