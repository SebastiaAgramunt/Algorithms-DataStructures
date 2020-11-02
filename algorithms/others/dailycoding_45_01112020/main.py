# Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
# with uniform probability, implement a function rand7() that returns an integer 
# from 1 to 7 (inclusive).


# Explanation:
# generate two numbers A and B between 0 and 4, muliply the first by 5 to get the
# possible values:
# 5*A = [0, 5, 10, 15, 20]
# now combined with the second possible values [0, 1, 2, 3, 4]
# we can generate fully from 0 to 24 uniformly random
# now 7*3 = 21, so we may generate from 0 to 21 to apply modulo 7 and get uniform random
# between 1 and 7. Therefore we discard numbers larger than 20

from random import seed, randint
from collections import Counter

def rand5():
    # rdm [1, 5] both included
    return randint(1, 5)


def rand7():
    while True:
        n = 5*(rand5() - 1) + (rand5() - 1)
        if n < 21:
            return n%7+1



if __name__ == "__main__":
    seed(1)
    n_items = int(1e6)
    vals = [rand7() for _ in range(n_items)]

    c = Counter(vals)
    for key in c:
        print(f"{key} percentage {c[key]/n_items}")


