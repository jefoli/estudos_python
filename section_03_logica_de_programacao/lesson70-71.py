# 70-71. while - Qual letra apareceu mais vezes na frase? (Iterando strings com while)
"""tarefa - Qual a letra apareceu mais vezes na frase.

Extra: var.count() -> O método count é utilizado para contar o número de ocorrências 
de um determinado caractere ou substring em uma string.
Ele retorna o número de vezes que o caractere ou substring aparece na string.
"""

phrase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

print(phrase)

i = 0
qtd_appears_more = 0
letter_appears_more = ''

while i < len(phrase):
    
    actual_letter = phrase[i]
    
    if actual_letter == ' ':
        i += 1
        continue

    qtd_show_letter = phrase.count(actual_letter)

    if qtd_appears_more < qtd_show_letter:
        qtd_appears_more = qtd_show_letter
        letter_appears_more = actual_letter
    
    i += 1

print(f'A letra que apareceu mais vezes foi "{letter_appears_more}" {qtd_appears_more}x')
