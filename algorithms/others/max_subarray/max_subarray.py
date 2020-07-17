import sys


def MaxSubArray(arr):
    n = len(arr)
    max_so_far = -sys.maxsize
    max_ending_here = 0

    # Agorithm that recursively finds the maximum of the subarray
    # finishing at index i.
    for i in range(0, n):

        # max subarray ending at i is maximum ending at i-1 plus
        # the value of the arr at i.
        max_ending_here = max_ending_here + arr[i]

        # if the value of arr[i] is larger than max_ending at i
        # then this value is the new maximum ending there
        if arr[i] > max_ending_here:
            max_ending_here = arr[i]

        # We have now the maximum ending at i, is this the maximum value found
        # so far?
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == "__main__":

    arr = [1, -13, 5, -8, 5, -3, 10]
    n = len(arr)
    print(MaxSubArray(arr))
