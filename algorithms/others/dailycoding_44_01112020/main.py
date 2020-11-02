# We can determine how "out of order" an array A is by counting the number of inversions it has. 
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] 
# has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] 
# has ten inversions: every distinct pair forms an inversion.


########################################################################################
'''
Procedure: we will use bubble sort, each time we are going to merge two arrays we count
the number of elements in the right that should've gone to the left and vice versa.
'''

from copy import deepcopy
from random import randrange, seed
import time

def brute_force_counts(arr):
    n = len(arr)
    counts = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                counts+=1
    return counts


def modified_mergesort(arr, counts=0):
    if len(arr) > 1:
        m = len(arr) // 2

        left_arr = arr[:m]
        right_arr = arr[m:]

        counts1 = modified_mergesort(left_arr, counts)
        counts2 = modified_mergesort(right_arr, counts)
        counts = counts1+counts2

        # now we merge the sorted arrays left and right
        i, j, k = 0, 0, 0

        len_left = len(left_arr)

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                counts+=(len_left - i)
            k += 1

        # at this point we have put all elements either of left or right
        # we have to complete until all elements are in the array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return counts



# driver code to test the above code
if __name__ == "__main__":
    seed(9)
    arr = [randrange(100) for _ in range(10000)]
    #arr = [2, 4, 1, 3, 5]

    start = time.perf_counter() 
    counts_merge = modified_mergesort(deepcopy(arr))
    mid = time.perf_counter() 
    counts_bruteforce = brute_force_counts(deepcopy(arr))
    end = time.perf_counter() 

    print(f"Time elapsed for brute force {end-mid}")
    print(f"Time elapsed for merge sort {mid-start}\n")
    print(f"Out of order pairs: {counts_merge}")


    assert counts_merge == counts_bruteforce, "algoirthm not well implemented"



