package main

import (
	"fmt"
)

// insertion 将array[i]插入到已排序的子数组array[0:i]中的适当位置
func insertion(array []int, i int) {
	key := array[i]
	j := i - 1
	for j >= 0 && array[j] > key {
		array[j+1] = array[j]
		j -= 1
	}
	array[j+1] = key
}

// insertionSort 对数组array进行插入排序
func insertionSort(array []int, n int) {
	for i := 1; i < n; i++ {
		insertion(array, i)
	}
}

func main() {
	array := []int{22, 27, 16, 2, 18, 6}
	insertionSort(array, len(array))
	fmt.Println("Sorted array is:", array)
}
