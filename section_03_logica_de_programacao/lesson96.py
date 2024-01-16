# 96. Desempacotamento em chamadas de funções

string = 'ABCD'

lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']

tupla = 'Python', 'é', 'legal'

# ap -> pega o antepenúltimo
# u -> pega o último valor

a, b, *_, ap, u = lista

print(a, u, ap) 

# desempacotar a lista c/ (*):
print(*lista)
print(*string, sep='-')

# desempacotamos e deixamos todos valores na mesma linha:
for nome in lista:
    print(nome, end=' ')


salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda'],
]

print(*salas, sep='\n')