# 96. Desempacotamento em chamadas de funções
string = 'ABCD'

lista_sortida = ['Maria', 'Helena', 1,2,3, 'Eduarda']

tupla = 'Python', 'é', 'legal'

primeiro_valor, segundo_valor, *_, penultimo_valor, ultimo_valor = lista_sortida

print(primeiro_valor, ultimo_valor, penultimo_valor) 

# desempacotar a lista_sortida c/ (*):
print(*lista_sortida)
print(*string, sep='-')

# desempacotamos e deixamos todos valores na mesma linha:
for nome in lista_sortida:
    print(nome, end=' ')


salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda'],
]

print(*salas, sep='\n')