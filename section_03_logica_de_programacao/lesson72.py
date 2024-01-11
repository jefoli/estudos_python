# 72. Introdução ao for / in - estrutura de repetição para coisas finitas

text = 'python'

new_text = ''
for letter in text:
    new_text += f'*{letter}'
    print(letter)
print(new_text)