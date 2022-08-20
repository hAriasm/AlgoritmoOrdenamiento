package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

type minheap struct {
	arr []int
}

func newMinHeap(arr []int) *minheap {
	minheap := &minheap{
		arr: arr,
	}
	return minheap
}

func (m *minheap) leftchildIndex(index int) int {
	return 2*index + 1
}

func (m *minheap) rightchildIndex(index int) int {
	return 2*index + 2
}

func (m *minheap) swap(first, second int) {
	temp := m.arr[first]
	m.arr[first] = m.arr[second]
	m.arr[second] = temp
}

func (m *minheap) leaf(index int, size int) bool {
	if index >= (size/2) && index <= size {
		return true
	}
	return false
}

func (m *minheap) downHeapify(current int, size int) {
	if m.leaf(current, size) {
		return
	}
	smallest := current
	leftChildIndex := m.leftchildIndex(current)
	rightRightIndex := m.rightchildIndex(current)
	if leftChildIndex < size && m.arr[leftChildIndex] < m.arr[smallest] {
		smallest = leftChildIndex
	}
	if rightRightIndex < size && m.arr[rightRightIndex] < m.arr[smallest] {
		smallest = rightRightIndex
	}
	if smallest != current {
		m.swap(current, smallest)
		m.downHeapify(smallest, size)
	}
	return
}

func (m *minheap) buildMinHeap(size int) {
	for index := ((size / 2) - 1); index >= 0; index-- {
		m.downHeapify(index, size)
	}
}

func (m *minheap) sort(size int) {
	m.buildMinHeap(size)
	for i := size - 1; i > 0; i-- {
		// Move current root to end
		m.swap(0, i)
		m.downHeapify(0, i)
	}
}

func (m *minheap) print() {
	for _, val := range m.arr {
		fmt.Println(val)
	}
}

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
		var inputArray = data

		minHeap := newMinHeap(inputArray)

		start := time.Now()

		minHeap.sort(len(inputArray))

		elapsed := time.Since(start)
		fmt.Println(elapsed)

	}
}
