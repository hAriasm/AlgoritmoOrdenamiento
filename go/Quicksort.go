// Algoritmo :  QUICKSORT EN GOLANG

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

// ----------------------------------------------------------------------------------------
func quickSort(arr []int, low, high int) {
	if low < high {

		//Código para encuentrar el índice de pivote del límite inferior de un array
		var pivot = partition(arr, low, high)

		// Aplicar la estrategia de Dividir
		// para ordenar el lado izquierdo y el lado derecho de una matriz
		// respecto a la posicion del pivote

		// Lado izquierdo del array
		quickSort(arr, low, pivot-1)

		// Lado derecho del array
		quickSort(arr, pivot+1, high)
	}
}

// ---------------------------------------------------------------------------
func partition(arr []int, low, high int) int {

	// Se elije un elemento de límite inferior como valor pivote
	var pivot = arr[high]
	var i = low - 1
	var j int

	for j = low; j < high; j++ {

		if arr[j] <= pivot {
			i++
			var temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		}
	}

	var temp = arr[i+1]
	arr[i+1] = arr[high]
	arr[high] = temp

	return i + 1
}

// ---------------------------------------------------------------------------------

func main() {

	var fileDataList = []string{"../data/data_100.txt",
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
		"../data/data_500000.txt"}

	for i := range fileDataList {
		archivo, error := os.Open(fileDataList[i])
		if error != nil {
			fmt.Println("Hubo error")
		}
		scanner := bufio.NewScanner(archivo)
		data := []int{}
		for scanner.Scan() {
			i, err := strconv.Atoi(scanner.Text())
			if err != nil {
				panic(err)
			}
			data = append(data, i)
		}

		start := time.Now()
		quickSort(data, 0, len(data)-1)
		elapsed := time.Since(start)
		fmt.Printf("Tiempo de ejecución: %s    ", elapsed) // Aqui muestra todos los datos de tiempos de ejecución
		// fmt.Println(elapsed)
	}
}
