# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
Selection Sort: Neste algoritmo de ordenação, o primeiro elemento é assumido como o elemento mínimo. 
Em seguida, verificamos se um elemento menor que o mínimo assumido está presente no restante da lista. 
Se houver, trocamos o mínimo assumido pelo mínimo real. 
Caso contrário, passamos para o próximo elemento. 
O pior caso de tempo de execução é O(n^2) 1.
'''

lista = [3,7,9,398,1,2,1382,99,43, 65,49]

def selection_sort(arr):

    n_len = len(arr)

    for i in range(n_len):
        min_index = i
        for j in range(i+1, n_len):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

sort_3 = selection_sort(lista)
print('Selection Sort: ', sort_3)