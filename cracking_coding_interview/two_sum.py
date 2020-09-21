# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

from typing import List

def twosum(l: List[int], k):
    hashmap = {}
    for elem in l:
        if elem<0:
            raise ValueError(f"{elem} is not positive, all elements in list must be positive")
        remaining = k - elem
        if remaining in hashmap.keys():
            return True
        hashmap[elem] = remaining

    return False


if __name__ == "__main__":
    l = [10, 15, 3, 7]
    k = 17

    print(twosum(l, k))