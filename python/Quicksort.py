# ALGORITMO QUICKSORT EN PYTHON
from timeit import default_timer
from random import randint
import numpy as np
from random import randint
# función para encontrar la posición de la partición
def partition(array, low, high):

  # elige el elemento más a la derecha como pivote
  pivot = array[high]

  # puntero para mayor elemento
  i = low - 1

   # atravesar todos los elementos
  # comparar cada elemento con pivote
  for j in range(low, high):
    if array[j] <= pivot:
      
      # si se encuentra un elemento más pequeño que el pivote
      # intercambiarlo con el elemento mayor señalado por i
      i = i + 1

     # intercambiar elemento en i con elemento en j
      (array[i], array[j]) = (array[j], array[i])

  # intercambiar el elemento pivote con el elemento mayor especificado por i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # devuelve la posición desde donde se realiza la partición
  return i + 1

# Función que desarrolla el algoritmo quicksort
def quickSort(array, low, high):
  if low < high:

    
    # encontrar un elemento pivote tal que
    # elementos más pequeños que el pivote están a la izquierda
    # elementos mayores que el pivote están a la derecha
    pi = partition(array, low, high)

    
    # llamada recursiva a la izquierda del pivote
    quickSort(array, low, pi - 1)

   # llamada recursiva a la derecha del pivote
    quickSort(array, pi + 1, high)

datoss = ["../data/data_100.txt",
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
for x in range(0,len(datoss)):
  a2 = np.loadtxt(datoss[x], dtype=int)
  data = a2.tolist()
  size = len(data)
  inicio = default_timer()
  quickSort(data, 0, size - 1)
  fin = default_timer()
  print('Tiempo de ejecución:', fin-inicio)
  