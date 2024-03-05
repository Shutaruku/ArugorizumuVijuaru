from typing import List

def selection_sort(A:List[int], N:int):
    # 定義找到子陣列中最小元素索引的函數
    def minimum(A:List[int], start:int, N:int):
        min_index = start
        for j in range(start + 1, N):
            if A[j] < A[min_index]:
                min_index = j
        return min_index
    
    # 進行選擇排序
    for i in range(N-1):
        # 找到從i到N之間最小元素的索引
        minj = minimum(A, i, N)
        # 交換當前元素與找到的最小元素
        A[i], A[minj] = A[minj], A[i]

def main():
    # 測試選擇排序函數
    A = [64, 25, 12, 22, 11]
    N = len(A)
    selection_sort(A, N)
    print("Sorted array is:", A)

if __name__ == "__main__":
    main()
