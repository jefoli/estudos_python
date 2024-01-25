# Exercício - Algoritmos de ordenação(Quicksort, Bubble, Sort Selection Sort, Merge Sort, Heap Sort)
'''
Merge Sort: Este é um algoritmo de ordenação dividir e conquistar. 
Ele divide a lista em duas metades, ordena cada metade e, em seguida, 
mescla as duas metades ordenadas para produzir a lista final ordenada. 
O pior caso de tempo de execução é O(n log n) 1.

'''
lista = [3,7,9,398,1,2,1382,99,43, 65,49]

def merge_sort(arr):
    number_len = len(arr)
    
    if number_len <= 1:
        return arr
    
    half = number_len // 2
    left = arr[:half]
    right = arr[half:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]

    return result

sort_5 = merge_sort(lista)
print('Merge Sort: ', sort_5)