from typing import List

def insertion(A: List[int], i: int) -> None:
    """
    將A[i]插入到已排序的子陣列A[0:i]中的適當位置
    """
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key

def insertionSort(A: List[int], N: int) -> None:
    """
    對陣列A進行插入排序
    """
    for i in range(1, N):
        insertion(A, i)

# 測試代碼
if __name__ == "__main__":
    A = [22, 27, 16, 2, 18, 6]
    N = len(A)
    insertionSort(A, N)
    print("Sorted array is:", A)
