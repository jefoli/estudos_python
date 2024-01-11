# 69. while / else (recurso peculiar do Python)
# pouco utilizado, mas temos essa possibilidade.
# Se tivermos um BREAK dentro do while, o ELSE não será executado!

string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    
    if letra == ' ':
        print("Passei aqui!")
        break
    i += 1
    
else:
    print("Else executado")