# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
Insertion Sort: Este algoritmo de ordenação é semelhante ao Bubble Sort, 
mas é mais eficiente em termos de tempo de execução. 
Ele divide a lista em duas partes: uma parte ordenada e outra desordenada. 
Em seguida, ele percorre a lista desordenada e insere cada elemento na posição correta na lista ordenada. 
O pior caso de tempo de execução é O(n^2) 1.

'''

lista = [3,7,9,398,1,2,1382,99,43,65,49]

def insertion_sort(arr):
    n_len = len(arr)

    for i in range (1, n_len):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

sort_4 = insertion_sort(lista)
print('Insertion Sort: ', sort_4)