
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(list, item):
    baixo = 0
    alto = len(list) - 1


    while baixo <= alto:
        meio = (alto + baixo) // 2 # Verifica o elemento central da lista
        chute = list[meio] # pega o objeto do indice

        if chute == item:
            return meio
        
        if chute > item:
            alto = meio - 1 # alto recebe metade do valor - 1
            print(alto)
        else:
            baixo = meio + 1
    return None


print(binary_search(list_number, item = 4))