# given a list of numbers calculate all permutations
from typing import List
import time


def add_number(num: int, nums: List[List[int]]) -> List[List[int]]:

    output = []
    for l in nums:
        for i in range(0, len(l) + 1):
            l2 = l.copy()
            l2.insert(i, num)
            output.append(l2)
    return output


def permutations(nums: List[int]) -> List[List[int]]:
    l = [[]]
    for i in nums:
        l = add_number(i, l)
    return l


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":

    # number of elements in list
    n = 3
    nums = list(range(0, n, 1))

    print("This is the initial list:\n{}".format(nums))

    t_i = time.time()
    l = permutations(nums)

    print("all permutations:\n{}".format(l))

    print("Time elapsed during calculation {} seconds".format(time.time() - t_i))

    print("Expected n!={} and got {} elements in list".format(factorial(n), len(l)))
