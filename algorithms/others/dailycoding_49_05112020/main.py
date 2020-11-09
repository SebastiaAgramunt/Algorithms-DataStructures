# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 

#since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.

from typing import List

def maxsum(arr: List[int]) -> int:
    max_so_far = 0
    max_now = 0

    for i in arr:
        if i > 0:
            max_now += i
            if max_now > max_so_far:
                max_so_far = max_now
        else:
            max_now = 0

    return max_so_far


if __name__ == "__main__":
    arr = [34, -50, 42, 14, -5, 86]
    m = maxsum(arr)

    print(f"The array is:\n{arr}")
    print(f"maxsum is:\n{m}")