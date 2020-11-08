from random import randrange, seed
from copy import deepcopy
from typing import List
from time import perf_counter
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=False, type=str, help="output fiile")
ap.add_argument("-n", "--maxn", required=True, type=int, help="max length of the list")
ap.add_argument("-s", "--seed", required=True, type=int, default=123, help="seed to generate random lists")



def mergesort(arr: List[int]) -> None:
    if len(arr)>1:

        m = len(arr)//2

        left_arr = arr[:m]
        right_arr = arr[m:]

        mergesort(left_arr)
        mergesort(right_arr)

        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k +=1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k +=1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        m = partition(arr, low, high)
        quicksort(arr, low, m-1)
        quicksort(arr, m+1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def bubblesort(arr: List[int]) -> None:
    n = len(arr)

    aSwap = True

    # Do while there is a pass without any swaps
    while aSwap:
        aSwap = False
        for i in range(0, n - 1):
            # compare one with the next
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                aSwap = True

if __name__ == "__main__":

    # python algorithms/sorting/sorting_comparisons.py -n 4000 -s 1  -f sorting_comparison.csv

    args = vars(ap.parse_args())

    filename = args["file"]
    maxn = args["maxn"]
    s = args["seed"]

    maxval = 999999

    if filename:
        with open(filename, "w+") as file:
            file.write("N,mergesort,quicksort,bubblesort\n")

    seed(s)
    for n in range(2, maxn):
        arr = [randrange(maxval) for _ in range(n)]

        to_mergesort = deepcopy(arr)
        to_quicksort = deepcopy(arr)
        to_bubblesort = deepcopy(arr)

        start_merge = perf_counter()
        mergesort(to_mergesort)
        end_merge = perf_counter()

        start_quicksort = perf_counter()
        quicksort(to_quicksort, 0, len(to_quicksort)-1)
        end_quicksort = perf_counter()

        start_bubble = perf_counter()
        bubblesort(to_bubblesort)
        end_bubble = perf_counter()

        print(f"N: {n}\n\t")
        print(f"Time elapsed mergesort:\n\t{end_merge - start_merge}")
        print(f"Time elapsed quicksort:\n\t{end_quicksort - start_quicksort}")
        print(f"Time elapsed bubble:\n\t{end_bubble - start_bubble}")

        if filename:
            with open(filename, "a+") as file:
                file.write(f"{n},{end_merge - start_merge},{end_quicksort - start_quicksort},{end_bubble - start_bubble}\n")
