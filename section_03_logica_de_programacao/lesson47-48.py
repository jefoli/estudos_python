''' 47. Exercício: teste seu conhecimento até aqui

1) Peça ao usuário para digitar seu nome
2) Peça ao usuário para digitar sua idade

#Regra de negócio

Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba 'Desculpe, você deixou campos vazios'

'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade !='':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios!')