package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

func mergeSort(items []int) []int {
	if len(items) < 2 {
		return items
	}
	first := mergeSort(items[:len(items)/2])
	second := mergeSort(items[len(items)/2:])
	return merge(first, second)
}

func merge(a []int, b []int) []int {
	final := []int{}
	i := 0
	j := 0
	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			final = append(final, a[i])
			i++
		} else {
			final = append(final, b[j])
			j++
		}
	}
	for ; i < len(a); i++ {
		final = append(final, a[i])
	}
	for ; j < len(b); j++ {
		final = append(final, b[j])
	}
	return final
}

func main() {

	//Lectura de 100 datos
	archivo_100, error := os.Open("../data/data_100.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_100 := bufio.NewScanner(archivo_100)
	data_100 := []int{}

	for scanner_100.Scan() {
		i, err := strconv.Atoi(scanner_100.Text())
		if err != nil {
			panic(err)
		}
		data_100 = append(data_100, i)
	}
	var array_100 = data_100

	// Inicio temporizador 100 datos
	start_100 := time.Now()
	mergeSort(array_100)
	elapsed_100 := time.Since(start_100)
	fmt.Println(elapsed_100)

	//Lectura de 1000 datos
	archivo_1000, error := os.Open("../data/data_1000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_1000 := bufio.NewScanner(archivo_1000)
	data_1000 := []int{}

	for scanner_1000.Scan() {
		i, err := strconv.Atoi(scanner_1000.Text())
		if err != nil {
			panic(err)
		}
		data_1000 = append(data_1000, i)
	}
	var array_1000 = data_1000

	// Inicio temporizador 1000 datos
	start_1000 := time.Now()
	mergeSort(array_1000)
	elapsed_1000 := time.Since(start_1000)
	fmt.Println(elapsed_1000)

	//Lectura de 2000 datos
	archivo_2000, error := os.Open("../data/data_2000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_2000 := bufio.NewScanner(archivo_2000)
	data_2000 := []int{}

	for scanner_2000.Scan() {
		i, err := strconv.Atoi(scanner_2000.Text())
		if err != nil {
			panic(err)
		}
		data_2000 = append(data_2000, i)
	}
	var array_2000 = data_2000

	// Inicio temporizador 2000 datos
	start_2000 := time.Now()
	mergeSort(array_2000)
	elapsed_2000 := time.Since(start_2000)
	fmt.Println(elapsed_2000)

	//Lectura de 3000 datos
	archivo_3000, error := os.Open("../data/data_3000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_3000 := bufio.NewScanner(archivo_3000)
	data_3000 := []int{}

	for scanner_3000.Scan() {
		i, err := strconv.Atoi(scanner_3000.Text())
		if err != nil {
			panic(err)
		}
		data_3000 = append(data_3000, i)
	}
	var array_3000 = data_3000

	// Inicio temporizador 3000 datos
	start_3000 := time.Now()
	mergeSort(array_3000)
	elapsed_3000 := time.Since(start_3000)
	fmt.Println(elapsed_3000)

	//Lectura de 4000 datos
	archivo_4000, error := os.Open("../data/data_4000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_4000 := bufio.NewScanner(archivo_4000)
	data_4000 := []int{}

	for scanner_4000.Scan() {
		i, err := strconv.Atoi(scanner_4000.Text())
		if err != nil {
			panic(err)
		}
		data_4000 = append(data_4000, i)
	}
	var array_4000 = data_4000

	// Inicio temporizador 4000 datos
	start_4000 := time.Now()
	mergeSort(array_4000)
	elapsed_4000 := time.Since(start_4000)
	fmt.Println(elapsed_4000)

	//Lectura de 5000 datos
	archivo_5000, error := os.Open("../data/data_5000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_5000 := bufio.NewScanner(archivo_5000)
	data_5000 := []int{}

	for scanner_5000.Scan() {
		i, err := strconv.Atoi(scanner_5000.Text())
		if err != nil {
			panic(err)
		}
		data_5000 = append(data_5000, i)
	}
	var array_5000 = data_5000

	// Inicio temporizador 5000 datos
	start_5000 := time.Now()
	mergeSort(array_5000)
	elapsed_5000 := time.Since(start_5000)
	fmt.Println(elapsed_5000)

	//Lectura de 6000 datos
	archivo_6000, error := os.Open("../data/data_6000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_6000 := bufio.NewScanner(archivo_6000)
	data_6000 := []int{}

	for scanner_6000.Scan() {
		i, err := strconv.Atoi(scanner_6000.Text())
		if err != nil {
			panic(err)
		}
		data_6000 = append(data_6000, i)
	}
	var array_6000 = data_6000

	// Inicio temporizador 6000 datos
	start_6000 := time.Now()
	mergeSort(array_6000)
	elapsed_6000 := time.Since(start_6000)
	fmt.Println(elapsed_6000)

	//Lectura de 7000 datos
	archivo_7000, error := os.Open("../data/data_7000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_7000 := bufio.NewScanner(archivo_7000)
	data_7000 := []int{}

	for scanner_7000.Scan() {
		i, err := strconv.Atoi(scanner_7000.Text())
		if err != nil {
			panic(err)
		}
		data_7000 = append(data_7000, i)
	}
	var array_7000 = data_7000

	// Inicio temporizador 7000 datos
	start_7000 := time.Now()
	mergeSort(array_7000)
	elapsed_7000 := time.Since(start_7000)
	fmt.Println(elapsed_7000)

	//Lectura de 8000 datos
	archivo_8000, error := os.Open("../data/data_8000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_8000 := bufio.NewScanner(archivo_8000)
	data_8000 := []int{}

	for scanner_8000.Scan() {
		i, err := strconv.Atoi(scanner_8000.Text())
		if err != nil {
			panic(err)
		}
		data_8000 = append(data_8000, i)
	}
	var array_8000 = data_8000

	// Inicio temporizador 8000 datos
	start_8000 := time.Now()
	mergeSort(array_8000)
	elapsed_8000 := time.Since(start_8000)
	fmt.Println(elapsed_8000)

	//Lectura de 9000 datos
	archivo_9000, error := os.Open("../data/data_9000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_9000 := bufio.NewScanner(archivo_9000)
	data_9000 := []int{}

	for scanner_9000.Scan() {
		i, err := strconv.Atoi(scanner_9000.Text())
		if err != nil {
			panic(err)
		}
		data_9000 = append(data_9000, i)
	}
	var array_9000 = data_9000

	// Inicio temporizador 9000 datos
	start_9000 := time.Now()
	mergeSort(array_9000)
	elapsed_9000 := time.Since(start_9000)
	fmt.Println(elapsed_9000)

	//Lectura de 10000 datos
	archivo_10000, error := os.Open("../data/data_10000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_10000 := bufio.NewScanner(archivo_10000)
	data_10000 := []int{}

	for scanner_10000.Scan() {
		i, err := strconv.Atoi(scanner_10000.Text())
		if err != nil {
			panic(err)
		}
		data_10000 = append(data_10000, i)
	}
	var array_10000 = data_10000

	// Inicio temporizador 10000 datos
	start_10000 := time.Now()
	mergeSort(array_10000)
	elapsed_10000 := time.Since(start_10000)
	fmt.Println(elapsed_10000)

	//Lectura de 20000 datos
	archivo_20000, error := os.Open("../data/data_20000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_20000 := bufio.NewScanner(archivo_20000)
	data_20000 := []int{}

	for scanner_20000.Scan() {
		i, err := strconv.Atoi(scanner_20000.Text())
		if err != nil {
			panic(err)
		}
		data_20000 = append(data_20000, i)
	}
	var array_20000 = data_20000

	// Inicio temporizador 20000 datos
	start_20000 := time.Now()
	mergeSort(array_20000)
	elapsed_20000 := time.Since(start_20000)
	fmt.Println(elapsed_20000)

	//Lectura de 30000 datos
	archivo_30000, error := os.Open("../data/data_30000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_30000 := bufio.NewScanner(archivo_30000)
	data_30000 := []int{}

	for scanner_30000.Scan() {
		i, err := strconv.Atoi(scanner_30000.Text())
		if err != nil {
			panic(err)
		}
		data_30000 = append(data_30000, i)
	}
	var array_30000 = data_30000

	// Inicio temporizador 30000 datos
	start_30000 := time.Now()
	mergeSort(array_30000)
	elapsed_30000 := time.Since(start_30000)
	fmt.Println(elapsed_30000)

	//Lectura de 40000 datos
	archivo_40000, error := os.Open("../data/data_40000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_40000 := bufio.NewScanner(archivo_40000)
	data_40000 := []int{}

	for scanner_40000.Scan() {
		i, err := strconv.Atoi(scanner_40000.Text())
		if err != nil {
			panic(err)
		}
		data_40000 = append(data_40000, i)
	}
	var array_40000 = data_40000

	// Inicio temporizador 40000 datos
	start_40000 := time.Now()
	mergeSort(array_40000)
	elapsed_40000 := time.Since(start_40000)
	fmt.Println(elapsed_40000)

	//Lectura de 50000 datos
	archivo_50000, error := os.Open("../data/data_50000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_50000 := bufio.NewScanner(archivo_50000)
	data_50000 := []int{}

	for scanner_50000.Scan() {
		i, err := strconv.Atoi(scanner_50000.Text())
		if err != nil {
			panic(err)
		}
		data_50000 = append(data_50000, i)
	}
	var array_50000 = data_50000

	// Inicio temporizador 50000 datos
	start_50000 := time.Now()
	mergeSort(array_50000)
	elapsed_50000 := time.Since(start_50000)
	fmt.Println(elapsed_50000)

	//Lectura de 100000 datos
	archivo_100000, error := os.Open("../data/data_100000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_100000 := bufio.NewScanner(archivo_100000)
	data_100000 := []int{}

	for scanner_100000.Scan() {
		i, err := strconv.Atoi(scanner_100000.Text())
		if err != nil {
			panic(err)
		}
		data_100000 = append(data_100000, i)
	}
	var array_100000 = data_100000

	// Inicio temporizador 100000 datos
	start_100000 := time.Now()
	mergeSort(array_100000)
	elapsed_100000 := time.Since(start_100000)
	fmt.Println(elapsed_100000)

	//Lectura de 200000 datos
	archivo_200000, error := os.Open("../data/data_200000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_200000 := bufio.NewScanner(archivo_200000)
	data_200000 := []int{}

	for scanner_200000.Scan() {
		i, err := strconv.Atoi(scanner_200000.Text())
		if err != nil {
			panic(err)
		}
		data_200000 = append(data_200000, i)
	}
	var array_200000 = data_200000

	// Inicio temporizador 200000 datos
	start_200000 := time.Now()
	mergeSort(array_200000)
	elapsed_200000 := time.Since(start_200000)
	fmt.Println(elapsed_200000)

	//Lectura de 300000 datos
	archivo_300000, error := os.Open("../data/data_300000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_300000 := bufio.NewScanner(archivo_300000)
	data_300000 := []int{}

	for scanner_300000.Scan() {
		i, err := strconv.Atoi(scanner_300000.Text())
		if err != nil {
			panic(err)
		}
		data_300000 = append(data_300000, i)
	}
	var array_300000 = data_300000

	// Inicio temporizador 300000 datos
	start_300000 := time.Now()
	mergeSort(array_300000)
	elapsed_300000 := time.Since(start_300000)
	fmt.Println(elapsed_300000)

	//Lectura de 400000 datos
	archivo_400000, error := os.Open("../data/data_400000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_400000 := bufio.NewScanner(archivo_400000)
	data_400000 := []int{}

	for scanner_400000.Scan() {
		i, err := strconv.Atoi(scanner_400000.Text())
		if err != nil {
			panic(err)
		}
		data_400000 = append(data_400000, i)
	}
	var array_400000 = data_400000

	// Inicio temporizador 400000 datos
	start_400000 := time.Now()
	mergeSort(array_400000)
	elapsed_400000 := time.Since(start_400000)
	fmt.Println(elapsed_400000)

	//Lectura de 500000 datos
	archivo_500000, error := os.Open("../data/data_500000.txt")
	if error != nil {
		fmt.Println("Hubo error")
	}
	scanner_500000 := bufio.NewScanner(archivo_500000)
	data_500000 := []int{}

	for scanner_500000.Scan() {
		i, err := strconv.Atoi(scanner_500000.Text())
		if err != nil {
			panic(err)
		}
		data_500000 = append(data_500000, i)
	}
	var array_500000 = data_500000

	// Inicio temporizador 500000 datos
	start_500000 := time.Now()
	mergeSort(array_500000)
	elapsed_500000 := time.Since(start_500000)
	fmt.Println(elapsed_500000)

}
