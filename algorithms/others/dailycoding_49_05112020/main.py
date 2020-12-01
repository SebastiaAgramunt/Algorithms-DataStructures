# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 

#since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

from typing import List

def maxsum(arr: List[int]) -> int:
    max_so_far = 0
    max_here = 0

    for i in arr:

        # max at this point can be the previous max + the current element
        max_here += i

        # if the max ending here is larger than the already found, set it as max
        if max_here > max_so_far:
            max_so_far = max_here

        # if we reach negative values ending here, just set max_here to zero
        if max_here < 0:
            max_here = 0

    return max_so_far


if __name__ == "__main__":
    arr = [34, -50, 42, 14, -5, 86]
    m = maxsum(arr)

    print(f"The array is:\n{arr}")
    print(f"maxsum is:\n{m}")