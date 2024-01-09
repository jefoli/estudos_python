#função PRINT
# NÃO PODE ESCREVER print com a primeira letra em maiúsculo

# exp errado: Print


#sep= -> separador!!!
# sep=' ' <- por padrão

#print -> utilizado para exibir algo na tela


#dentro de parenteses passamos argumentos para funções

#print com 2 argumentos:
print(12, 34, sep=' ')
print(12, 44, sep='-')

#DICA -> clicar em cima da linha e crtlC + crtlV () -> duplica tudo de uma vez sem a necessidade de ficar copiando e colando com o mouse

print(56, 78)
print()

#descrito no vscode - menu
#CRLF-> QUEBRA DE LINHA ESPECÍFICA DO WINDOWS. Seus caracteres são \r\n (faz com que o pc quebre a linha)

# end='' -> significa o final do print

print(20,30,33, end='\r\n') #esse é o padrão do sistema windows
print(20,30,33, sep='--', end='##eeeed') #podemos colocar outras coisas
print(20,30,33, end='##eeeed') #podemos colocar outras coisas

#print(20,304,33, end='\r') #esse é o padrão do sistema UNIX