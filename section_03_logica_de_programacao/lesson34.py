# 34. Introdução aos blocos de código + if / elif / else (condicionais)

#ESTRUTURAS CONDICIONAIS -> altera o fluxo do código

# IF - ELSE (se-senão)

# IF - ELIF - ELSE (se / se-não-se / senão)

#NÃO ESQUECER DE COLOCAR : (dois pontos após o  if )

#fórmula: if <condicionais> : <saída>

# OBS: ELE VAI EXECUTAR SOMENTE A PRIMEIRA CONDIÇÃO VERDADEIRA

entrada = input('Você quer "entrar" ou "sair"?')

#exemplo com if:
# if + condução
# temos que colocar identação (4 espaços de tab!)

#pode ser:

# only IF: if == 'entrar': print('')

# IF + ELSE: if == 'entrar': print('') else: print('Você não digitou entrar ou sair')

#IF + ELIF + ELSE: 

if entrada == "entrar":
  print('Você entrou no sistema')
elif entrada == 'sair':
  print('Você saiu no sistema')
else:
  print('Você não digitou entrar ou sair')

# OBS: ELE VAI EXECUTAR SOMENTE A PRIMEIRA CONDIÇÃO VERDADEIRA

#podemos colocar mais de um elif
