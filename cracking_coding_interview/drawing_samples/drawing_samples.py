# Imagine we have a probability distribution as follows
# pr = [0.2, 0.3, 0.1, 0.4] correspoding to numbers
# n = [0, 1, 2, 3]
# write a function that draws k elements of this distribution

from random import random, seed
from collections import Counter
from typing import List


def binary_search(cum_sum, low, high, val):

    if high >= low:
        m = low + (high - low) // 2

        if m == 0:
            return m

        if m == len(cum_sum) - 1:
            return m

        if val < cum_sum[m + 1] and val > cum_sum[m]:
            return m + 1

        elif val > cum_sum[m - 1] and val < cum_sum[m]:
            return m

        else:
            if val > cum_sum[m]:
                return binary_search(cum_sum, m + 1, high, val)
            else:
                return binary_search(cum_sum, low, m - 1, val)
    else:
        return None


def draw_distrib(pr: List[float], k: int) -> List[int]:
    cum_sum = []
    c = 0

    # write cumulative sum
    # [0.2, 0.5, 0.6, 1.0]
    for i in pr:
        c += i
        cum_sum.append(c)

    rdm_elements = []
    # draw k elements
    for _ in range(k):
        x = random()  # float between 0.0 and 1.0
        i = binary_search(cum_sum, 0, len(cum_sum) - 1, x)
        rdm_elements.append(i)

    return rdm_elements


if __name__ == "__main__":

    seed(1)
    pr = [0.2, 0.3, 0.1, 0.4]
    k = 2000
    assert sum(pr) > 0.999 and sum(pr) < 1.0001, "Probabilities don't add up to 1.0"

    a = draw_distrib(pr, k)
    count = Counter(a)

    for elem in count:
        print(f"Probability of {elem} is {count[elem]/k}")
