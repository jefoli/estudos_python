# 54-57. Exercícios - Enunciados
''' 
Exercício 1:

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número inteiro é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

'''
escolha_um_numero = input("Digite um número inteiro: ")

# 1 forma:
if escolha_um_numero.isdigit():
    valor_entrada = int(escolha_um_numero) % 2
    if valor_entrada == 0:
        print("Numero Par!")
    else:
        print("Número Impar!") 
else:
    print("Você não digitou um número inteiro!")

# 2 forma:
if escolha_um_numero.isdigit():   
    valor_entrada = int(escolha_um_numero)
    calculadora_par_impar = valor_entrada  % 2 == 0
    par_impar_texto = "ímpar"
    if calculadora_par_impar:
        par_impar_texto = "par"
    print("Número Par!")
else:
    print("Você não digitou um número inteiro!")


# 3 forma
try:
    calculadora = int(escolha_um_numero) % 2
    #print(calculadora)
    if calculadora == 0:
        print("Número Par!")
    else:
        print("Número Impar!") 
except:
    print("Você não digitou um número inteiro!")


''' 
Exercício 2:

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada.

Exemplo: Bom dia (0-11h), Boa tarde (12-17h) e Boa noite (18-23h).

'''

hora = input("Digite a hora: ")
try:
    converte_hora = int(hora)
    if converte_hora >= 0 and converte_hora <= 11:
        print('Bom dia')
    elif converte_hora >= 12 and converte_hora <= 17:
        print('Boa tarde')
    elif converte_hora >= 18 and converte_hora <= 23:
        print('Boa noite')
    else:
        print("Não conheço essa hora.")
except:
    print('Digite apenas números inteiros')


''' 
Exercício 3:

Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos, retorne "Seu nome é curto".
Se o nome tiver entre 5 a 6 letras, retorne "Seu nome é normal"
Se o nome tiver maior que 6 letras, retorne "Seu nome é muito grande"

'''
nome_usuario = input("Digite seu nome: ")
# print(len(nome_usuario))
qtd_caracteres = len(nome_usuario)

# 1 forma:
if qtd_caracteres <= 4:
    print('Seu nome é curto')
elif qtd_caracteres >= 5 and qtd_caracteres <= 6:
    print('seu nome é normal')
else:
    print('seu nome é grande')


# 2 forma c/ checagem:
if qtd_caracteres > 1:
    if qtd_caracteres <= 4:
        print('Seu nome é curto')
    elif qtd_caracteres >= 5 and qtd_caracteres <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é grande')
else:
    print('Digite mais de uma letra')
