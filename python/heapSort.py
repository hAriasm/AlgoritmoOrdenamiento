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

    # arr = np.loadtxt('..\data\data_50000.txt', dtype=int)

    datos = ["../data/data_100.txt",
              "../data/data_1000.txt",
              "../data/data_2000.txt",
              "../data/data_3000.txt",
              "../data/data_4000.txt",
              "../data/data_5000.txt",
              "../data/data_6000.txt",
              "../data/data_7000.txt",
              "../data/data_8000.txt",
              "../data/data_9000.txt",
              "../data/data_10000.txt",
              "../data/data_20000.txt",
              "../data/data_30000.txt",
              "../data/data_40000.txt",
              "../data/data_50000.txt",
              "../data/data_100000.txt",
              "../data/data_200000.txt",
              "../data/data_300000.txt",
              "../data/data_400000.txt",
              "../data/data_500000.txt"]
for i in range(0, len(datos)):
    arr = np.loadtxt(datos[i], dtype=int)
    inicio = time.time()
    heapSort(arr)
    fin = time.time()
    print(fin-inicio)
    root = None

# This code is contributed by Mohit Kumra
