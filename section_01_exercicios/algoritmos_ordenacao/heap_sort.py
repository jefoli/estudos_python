# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
Heap Sort: Este algoritmo de ordenação é baseado em árvore binária. 
Ele constrói uma árvore binária máxima a partir da lista de elementos e, 
em seguida, extrai o elemento máximo da raiz da árvore e o coloca no final da lista. 
O processo é repetido até que todos os elementos estejam ordenados. 
O pior caso de tempo de execução é O(n log n) 1.
'''

lista = [3,7,9,398,1,2,1382,99,43, 65,49]

def heap_sort(arr):
    numb_len = len(arr)

    for i in range(numb_len // 2 - 1, -1, -1):
        heapify(arr, numb_len, i)

    for i in range(numb_len - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, numb_len, i):
    greater = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < numb_len and arr[left] > arr[greater]:
        greater = left

    if right < numb_len and arr[right] > arr[greater]:
        greater = right

    if greater != i:
        arr[i], arr[greater] = arr[greater], arr[i]
        heapify(arr, numb_len, greater)

sort_6 = heap_sort(lista)
print('Heap Sort: ', sort_6)
        
