# Problem: Please find 95th percentile in a list of test scores.
# Solution: We use a quicksort variant. We know that the index at 95% percentile 
#           of a sorted array of size N int(0.95*N)
#           of length N 


from typing import List
from random import randrange, seed
from copy import deepcopy


def percent(arr: List[int], p: float) -> int:
    # Naive simple aproach NlogN
    assert p>0.0, "p has to be positive"
    assert p<1.0, "p has to be smaller than 1"

    # NlogN sorting
    arr.sort()
    i = int(len(arr)*p)

    return arr[i]


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]

    i = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickselect(arr: List[int], low: int, high: int, idx: int) -> int:
    # based on 
    # https://www.geeksforgeeks.org/quickselect-algorithm/
    # algorithm takes O(N) bc we only recur quickselect once
    # as compared to quicksort
    if low < high:
    
        m = partition(arr, low, high)

        if m == idx:
            return arr[m]
        elif m < idx:
            return quickselect(arr, m+1, high, idx)
        else:
            return quickselect(arr, low, m-1, idx)

    else:
        return arr[high]



if __name__ == "__main__":
    N = 100
    p = 0.95

    seed(2)

    arr = [randrange(N) for _ in range(N)]
    print(f"this is original array:\n{arr}")

    # i = percent(deepcopy(arr), p)
    # print(f"element at percentile {p}, {i}")
    sorted_array = deepcopy(arr)
    sorted_array.sort()
    print(f"This is the sorted array:\n{sorted_array}")


    # index a which we will find the element
    idx = int(len(arr)*p)
    i_2 = quickselect(deepcopy(arr), 0, len(arr)-1, idx)
    print(f"element at percentile {p}, {idx}")


