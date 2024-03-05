package main

import (
	"fmt"
)

// selectionSort 接受一個整數切片（slice）並對其進行選擇排序
func selectionSort(array []int) {
	n := len(array)
	for i := 0; i < n-1; i++ {
		// 查找從i到n之間最小元素的索引
		minIndex := i
		for j := i + 1; j < n; j++ {
			if array[j] < array[minIndex] {
				minIndex = j
			}
		}
		// 交換當前元素與找到的最小元素
		array[i], array[minIndex] = array[minIndex], array[i]
	}
}

func main() {
	// 測試選擇排序函數
	array := []int{64, 25, 12, 22, 11}
	selectionSort(array)
	fmt.Println("Sorted array is:", array)
}
