# 154. Modularização - Entendendo os seus próprios módulos e sys.path no Python
'''
- SEMPRE o primeiro módulo executado no python chama-se __main__

- Podemos importar outros módulos inteiros ou parte do módulo
    Obs: Tomar cuidado para colocar nome de módulo igual aos que já existem

- O Python conhece a pasta onde o __main__ está sendo executado abaixo dele

- Por padrão o Python não reconhece módulos acma do __main__ (exp: arquivo de outra pasta(pacotes))

- Python conhece todos os módulos e pacotes presentes nos caminhos sys.path

'''
import sys
#sys.path.append('/home') #adiciona um caminho no sistema (não é comum usar dessa forma)

import lesson153

print('Esse módulo se chama', __name__)
print(*sys.path, sep = '\n')