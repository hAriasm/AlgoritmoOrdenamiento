#------------------------------
# LIBRERIAS
#------------------------------
import numpy as np
import time

#------------------------------
# ALGORITMO DE ORDENAMIENTO
#------------------------------
def merge_sort(lista):
    if len (lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i+=1
            else:
                lista[k]=segunda_mitad[j]
                j+=1
            k+=1

        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i+=1
            k+=1

        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j+=1
            k+=1

#-----------------------------------------------------------
# LECTURA DE DATOS DE ARCHIVOS .TXT Y CONVERSION EN ARRAYs
#-----------------------------------------------------------
array_100 =np.loadtxt('..\data\data_100.txt',dtype=int)
array_1000 =np.loadtxt('..\data\data_1000.txt',dtype=int)
array_2000 =np.loadtxt('..\data\data_2000.txt',dtype=int)
array_3000 =np.loadtxt('..\data\data_3000.txt',dtype=int)
array_4000 =np.loadtxt('..\data\data_4000.txt',dtype=int)
array_5000 =np.loadtxt('..\data\data_5000.txt',dtype=int)
array_6000 =np.loadtxt('..\data\data_6000.txt',dtype=int)
array_7000 =np.loadtxt('..\data\data_7000.txt',dtype=int)
array_8000 =np.loadtxt('..\data\data_8000.txt',dtype=int)
array_9000 =np.loadtxt('..\data\data_9000.txt',dtype=int)
array_10000 =np.loadtxt('..\data\data_10000.txt',dtype=int)
array_20000 =np.loadtxt('..\data\data_20000.txt',dtype=int)
array_30000 =np.loadtxt('..\data\data_30000.txt',dtype=int)
array_40000 =np.loadtxt('..\data\data_40000.txt',dtype=int)
array_50000 =np.loadtxt('..\data\data_50000.txt',dtype=int)
array_100000 =np.loadtxt('..\data\data_100000.txt',dtype=int)
array_200000 =np.loadtxt('..\data\data_200000.txt',dtype=int)
array_300000 =np.loadtxt('..\data\data_300000.txt',dtype=int)
array_400000 =np.loadtxt('..\data\data_400000.txt',dtype=int)
array_500000 =np.loadtxt('..\data\data_500000.txt',dtype=int)

#-----------------------------------------------------------
# CONVERSION EN ARRAYs EN LISTAS
#-----------------------------------------------------------
lista_100=array_100.tolist()
lista_1000=array_1000.tolist()
lista_2000=array_2000.tolist()
lista_3000=array_3000.tolist()
lista_4000=array_4000.tolist()
lista_5000=array_5000.tolist()
lista_6000=array_6000.tolist()
lista_7000=array_7000.tolist()
lista_8000=array_8000.tolist()
lista_9000=array_9000.tolist()
lista_10000=array_10000.tolist()
lista_20000=array_20000.tolist()
lista_30000=array_30000.tolist()
lista_40000=array_40000.tolist()
lista_50000=array_50000.tolist()
lista_100000=array_100000.tolist()
lista_200000=array_200000.tolist()
lista_300000=array_300000.tolist()
lista_400000=array_400000.tolist()
lista_500000=array_500000.tolist()

#------------------------------------------------------------------
# EJECUCION DE PROGRAMAS DE ORDENAMIENTO PARA LISTAS DE "N" DATOS
#------------------------------------------------------------------

# Inicio de temporizador 100 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_100)
fin=time.time()
t_100= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_100)

# Inicio de temporizador 1000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_1000)
fin=time.time()
t_1000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_1000)

# Inicio de temporizador 2000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_2000)
fin=time.time()
t_2000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_2000)

# Inicio de temporizador 3000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_3000)
fin=time.time()
t_3000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_3000)

# Inicio de temporizador 4000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_4000)
fin=time.time()
t_4000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_4000)

# Inicio de temporizador 5000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_5000)
fin=time.time()
t_5000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_5000)

# Inicio de temporizador 6000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_6000)
fin=time.time()
t_6000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_6000)

# Inicio de temporizador 7000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_7000)
fin=time.time()
t_7000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_7000)

# Inicio de temporizador 8000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_8000)
fin=time.time()
t_8000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_8000)

# Inicio de temporizador 9000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_9000)
fin=time.time()
t_9000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_9000)

# Inicio de temporizador 10000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_10000)
fin=time.time()
t_10000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_10000)

# Inicio de temporizador 20000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_20000)
fin=time.time()
t_20000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_20000)

# Inicio de temporizador 30000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_30000)
fin=time.time()
t_30000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_30000)

# Inicio de temporizador 40000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_40000)
fin=time.time()
t_40000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_40000)

# Inicio de temporizador 50000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_50000)
fin=time.time()
t_50000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_50000)

# Inicio de temporizador 100000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_100000)
fin=time.time()
t_100000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_100000)

# Inicio de temporizador 200000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_200000)
fin=time.time()
t_200000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_200000)

# Inicio de temporizador 300000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_300000)
fin=time.time()
t_300000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_300000)

# Inicio de temporizador 400000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_400000)
fin=time.time()
t_400000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_400000)

# Inicio de temporizador 500000 datos
inicio = time.time()
# Ejecucion de programa de ordenamiento
merge_sort(lista_500000)
fin=time.time()
t_500000= fin-inicio
# Impresion de tiempo de ejecucion de programa
print(t_500000)