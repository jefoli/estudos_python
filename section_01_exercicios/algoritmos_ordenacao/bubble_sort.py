# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
Bubble Sort: Algoritmo de ordenação mais simples. 
Ele compara cada par adjacente e verifica se os elementos estão em ordem. 
Se não estiverem, os dois elementos são trocados. 
Esse processo é repetido até que todos os elementos estejam ordenados. 
O pior caso de tempo de execução é O(n^2), onde n é o número de elementos na lista:
'''

lista = [3,7,9,398,1,2,1382,99,43, 65,49]

def bubblesort(arr):
    
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sort_2 = bubblesort(lista)
print('Bubblesort: ', sort_2)