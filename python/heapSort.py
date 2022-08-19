# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

import numpy as np
from timeit import default_timer
import time



def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)

# The main function to sort an array of given size


def heapSort(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver's code
if __name__ == '__main__':
    # arr = [12, 11, 13, 5, 6, 7]

    arr = np.loadtxt('..\data\data_50000.txt', dtype=int)

array_100 = np.loadtxt('..\data\data_100.txt', dtype=int)
array_1000 = np.loadtxt('..\data\data_100.txt', dtype=int)
array_2000 = np.loadtxt('..\data\data_100.txt', dtype=int)
array_3000 = np.loadtxt('..\data\data_100.txt', dtype=int)
array_4000 = np.loadtxt('..\data\data_100.txt', dtype=int)
array_5000 = np.loadtxt('..\data\data_5000.txt', dtype=int)
array_6000 = np.loadtxt('..\data\data_6000.txt', dtype=int)
array_7000 = np.loadtxt('..\data\data_7000.txt', dtype=int)
array_8000 = np.loadtxt('..\data\data_8000.txt', dtype=int)
array_9000 = np.loadtxt('..\data\data_9000.txt', dtype=int)
array_10000 = np.loadtxt('..\data\data_10000.txt', dtype=int)
array_20000 = np.loadtxt('..\data\data_20000.txt', dtype=int)
array_30000 = np.loadtxt('..\data\data_30000.txt', dtype=int)
array_40000 = np.loadtxt('..\data\data_40000.txt', dtype=int)
array_50000 = np.loadtxt('..\data\data_50000.txt', dtype=int)
array_100000 = np.loadtxt('..\data\data_100000.txt', dtype=int)
array_200000 = np.loadtxt('..\data\data_200000.txt', dtype=int)
array_300000 = np.loadtxt('..\data\data_300000.txt', dtype=int)
array_400000 = np.loadtxt('..\data\data_400000.txt', dtype=int)
array_500000 = np.loadtxt('..\data\data_500000.txt', dtype=int)
array_1000000 = np.loadtxt('..\data\data_1000000.txt', dtype=int)
lista_100 = array_100.tolist()
lista_1000 = array_5000.tolist()
lista_2000 = array_5000.tolist()
lista_3000 = array_5000.tolist()
lista_4000 = array_5000.tolist()
lista_5000 = array_5000.tolist()
lista_6000 = array_6000.tolist()
lista_7000 = array_7000.tolist()
lista_8000 = array_8000.tolist()
lista_9000 = array_9000.tolist()
lista_10000 = array_10000.tolist()
lista_20000 = array_20000.tolist()
lista_30000 = array_30000.tolist()
lista_40000 = array_40000.tolist()
lista_50000 = array_50000.tolist()
lista_100000 = array_100000.tolist()
lista_200000 = array_200000.tolist()
lista_300000 = array_300000.tolist()
lista_400000 = array_400000.tolist()
lista_500000 = array_500000.tolist()
lista_1000000 = array_1000000.tolist()



inicio = time.time()
heapSort(lista_100)
fin=time.time()
t_100= fin-inicio
print(t_100)

inicio = time.time()
heapSort(lista_1000)
fin=time.time()
t_1000= fin-inicio
print(t_1000)

inicio = time.time()
heapSort(lista_2000)
fin=time.time()
t_2000= fin-inicio
print(t_2000)

inicio = time.time()
heapSort(lista_3000)
fin=time.time()
t_3000= fin-inicio
print(t_3000)

inicio = time.time()
heapSort(lista_4000)
fin=time.time()
t_4000= fin-inicio
print(t_4000)

inicio = time.time()
heapSort(lista_5000)
fin=time.time()
t_5000= fin-inicio
print(t_5000)

inicio = time.time()
heapSort(lista_5000)
fin=time.time()
t_5000= fin-inicio
print(t_5000)

inicio = time.time()
heapSort(lista_6000)
fin=time.time()
t_6000= fin-inicio
print(t_6000)

inicio = time.time()
heapSort(lista_7000)
fin=time.time()
t_7000= fin-inicio
print(t_7000)

inicio = time.time()
heapSort(lista_8000)
fin=time.time()
t_8000= fin-inicio
print(t_8000)

inicio = time.time()
heapSort(lista_9000)
fin=time.time()
t_9000= fin-inicio
print(t_9000)

inicio = time.time()
heapSort(lista_10000)
fin=time.time()
t_10000= fin-inicio
print(t_10000)

inicio = time.time()
heapSort(lista_20000)
fin=time.time()
t_20000= fin-inicio
print(t_20000)

inicio = time.time()
heapSort(lista_30000)
fin=time.time()
t_30000= fin-inicio
print(t_30000)

inicio = time.time()
heapSort(lista_40000)
fin=time.time()
t_40000= fin-inicio
print(t_40000)

inicio = time.time()
heapSort(lista_50000)
fin=time.time()
t_50000= fin-inicio
print(t_50000)

inicio = time.time()
heapSort(lista_100000)
fin=time.time()
t_100000= fin-inicio
print(t_100000)

inicio = time.time()
heapSort(lista_200000)
fin=time.time()
t_200000= fin-inicio
print(t_200000)

inicio = time.time()
heapSort(lista_300000)
fin=time.time()
t_300000= fin-inicio
print(t_300000)

inicio = time.time()
heapSort(lista_400000)
fin=time.time()
t_400000= fin-inicio
print(t_400000)

inicio = time.time()
heapSort(lista_500000)
fin=time.time()
t_500000= fin-inicio
print(t_500000)

inicio = time.time()
heapSort(lista_1000000)
fin=time.time()
t_1000000= fin-inicio
print(t_1000000)

# inicio = default_timer()
# # Function call
# heapSort(lista_100000)
# fin = default_timer()
# print('Tiempo de ejecucion:', fin-inicio)
 
# N = len(arr)

# print("Sorted array is")
# for i in range(N):
# print("%d" % arr[i], end=" ")
# This code is contributed by Mohit Kumra
