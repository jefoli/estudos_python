# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
O algoritmo Quick Sort é um algoritmo de ordenação por comparação que utiliza a abordagem “Dividir para Conquistar” para ordenar os elementos 1. 
O algoritmo funciona dividindo a lista de elementos em duas metades, 
ordenando cada metade e, em seguida, mesclando as duas metades ordenadas para produzir a lista final ordenada.
O algoritmo começa escolhendo um elemento da lista como pivô e particionando a lista em duas partes: 
uma parte com elementos menores que o pivô e outra parte com elementos maiores que o pivô. 
Em seguida, o algoritmo ordena recursivamente as duas partes da lista e as mescla para produzir a lista final ordenada.
O tempo de execução do Quick Sort depende do pivô escolhido. 
No pior caso, o tempo de execução é O(n^2), mas no caso médio, o tempo de execução é O(n log n) 1
'''

lista = [3,7,9,398,1,2,1382,99,43, 65,49]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

sort_1 = quick_sort(lista)
print('Quicksort: ', sort_1)