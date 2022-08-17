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

		// Find the pivot index of an lower bound of an array
		var pivot = partition(arr, low, high)

		// Apply Divide and conquer stratagy
		// to sort the left side and right side of an array
		// respective to the pivot position

		// Left hand side array
		quickSort(arr, low, pivot-1)

		// Right hand side array
		quickSort(arr, pivot+1, high)
	}
}

// ---------------------------------------------------------------------------
func partition(arr []int, low, high int) int {

	// Pick a lowest bound element as an pivot value
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

	archivo, error := os.Open("./data_1000000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner := bufio.NewScanner(archivo)
	datosPrueba := []int{}

	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		datosPrueba = append(datosPrueba, i)
	}

	var data = datosPrueba
	start := time.Now()
	quickSort(data, 0, len(data)-1) // aqui va su metodo de ordenamiento
	elapsed := time.Since(start)
	fmt.Printf("page took %s", elapsed)
}
