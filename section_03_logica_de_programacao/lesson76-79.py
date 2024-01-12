# 76-79 Exercício - Jogo da palavra secreta
'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.

- Iremos propor uma palavra secreta e vaidar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar a letra, deverá ser verificado se está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra;
    - Se a letra digita não estiver na palavra secra, exiba *;
- Faça a contagem de tentativas do usuário

'''
import os

palavra_secreta = 'perfurme'
letras_acertadas = ''
num_tentativas = 0

while True:
    
    letra_digitada = input('Digite digite uma letra: ')
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls') # limpa terminal - P/ linux ou mac usar os.system('clear')
        print('Você ganhou!!!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', num_tentativas)
        letras_acertadas = ''
        num_tentativas = 0
    
