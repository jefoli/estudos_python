#32. Formatação de strings com o método format
#objetos possuem métodos dentro
#objetos pode fazer algumas ações (suas ações são chamadas métodos)


#method - format

a = 'A'
b = 'B'
c = 1.1

#exemplo do método format:

formato = ''.format(a, b, c)

#format -> método
#parâmetros -> tudo dentro de ()


formato = 'a={} b={}'.format(a, b, c)
#como a chave está vazia, os argumentos são passados para dentro
print(formato)

#podemos colocar dentro de uma variável também:
string = 'a={} b={} c={:.2f}'

form = string.format(a,b,c)
print(form)

# se colocarmos uma quarta chave, irá ocorrer o seguinte erro -> out of range
# out of range = fora de alcance = acabou

#podemos reutilizar fora da ordem através dos ÍNDICES:

#invertemos a ordem através dos índices
string2 = 'a={0} b={2} c={1}'
form2 = string2.format(a, b, c)
print(form2)


#PARAMETRO NOMEADO -> quando damos um nome quando criamos ou damos nome a s funções
#tudo que vier depois de parâmetro nomeado precisa ser RENOMEADO

string4 = 'a={0} a={0} a={0} c={nome3:.2f}'

param_renamed = string4.format(
  a, b, nome3=c  

  #parâmetro -> nome3
  #argumento -> c(valor de c)
  #parâmetro + argumento = parâmetro nomeado!

  #Regra: se tivesse mais coisa na frente do C, teriamos que renomear as demais
)

print(param_renamed)