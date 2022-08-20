package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

func runningtime(s string) (string, time.Time) {
	log.Println("Start:	", s)
	return s, time.Now()
}

func track(s string, startTime time.Time) {
	endTime := time.Now()
	log.Println("End:	", s, "took", endTime.Sub(startTime))
}

type tree struct {
	value       int
	left, right *tree
}

// Sort sorts values in place.
func Sort(values []int) {
	var root *tree
	for _, v := range values {
		root = add(root, v)
	}
	appendValues(values[:0], root)
}

// appendValues appends the elements of t to values in order
// and returns the resulting slice.
func appendValues(values []int, t *tree) []int {
	if t != nil {
		values = appendValues(values, t.left)
		values = append(values, t.value)
		values = appendValues(values, t.right)
	}
	return values
}

func add(t *tree, value int) *tree {
	if t == nil {
		// Equivalent to return &tree{value: value}.
		t = new(tree)
		t.value = value
		return t
	}
	if value < t.value {
		t.left = add(t.left, value)
	} else {
		t.right = add(t.right, value)
	}
	return t
}

func execute() {

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
		Sort(data)
		elapsed := time.Since(start)
		fmt.Println(elapsed)

	}

}

func main() {
	execute()

}
