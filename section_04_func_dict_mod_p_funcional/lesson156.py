# 156. Recarregando módulos, importlib e singleton
'''
Todo módulo é singleton(carrega somente uma vez) - Após importar o módulo, 
o py salva ele na memória e toda vez que usar o import _modulo_,
não será importado novamente por questão de eficiência

Para recarregar um módulo, devemos usar -> import importlib

'''
#p/ recarregar o módulo
import importlib
import lesson155

#print(lesson155.multiplicar(4,5))

for i in range(3):
    importlib.reload(lesson155)
    print(i)
print('Módulo recarregado!')