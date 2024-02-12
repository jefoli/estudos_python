# 206. Exercício - Salve sua classe em JSON
'''
Salvar os dados da sua classe em JSON
e depois criar novamente as instâncias da classe com os dados salvos.
Salvar em um arquivo separado
'''
import json

FILE_PATH = 'lesson206.json'

class Person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def fazer_dump():
    with open(FILE_PATH, '+w', encoding='utf-8') as file:
        print('Fazendo DUMP...')
        json.dump(db, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    control = True
    
    db = []

    while control:

        nome_input = input('Nome: ')
        idade_input = input('Idade: ')
        injetar_pessoa = Person(nome_input, idade_input)
        db.append(vars(injetar_pessoa))
    
        print(vars(injetar_pessoa))
    
        check_input = input('Deseja continuar? ')
        if check_input != 's':
            break
    
    fazer_dump()