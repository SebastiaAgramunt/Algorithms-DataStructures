# Given a function that generates perfectly random numbers between 1 and k (inclusive), 
# where k is an input, write a function that shuffles a deck of cards represented 
# as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

from typing import List
from random import randrange, seed


import random 
def shuffle(arr: List[int]) -> None: 

    n = len(arr)
    for i in range(n-1,0,-1): 
        # Pick a random index from 0 to i 
        j = random.randrange(i+1) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 

# this make take some more time depending on the implementation of
# array in python (if it is linked list will take longer)
def shuffle2(arr: List[int]) -> List[int]:
    new_arr = []
    while len(arr)>0:
        i = randrange(len(arr))
        new_arr.append(arr[i])
        del arr[i]

    return new_arr

if __name__=='__main__': 
    seed(1)
    a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 
       9, 10, 11, 12, 13, 14, 15, 
       16, 17, 18, 19, 20, 21, 22,  
       23, 24, 25, 26, 27, 28, 29, 
       30, 31, 32, 33, 34, 35, 36, 
       37, 38, 39, 40, 41, 42, 43,  
       44, 45, 46, 47, 48, 49, 50, 
       51] 
    #arr2 = shuffle2(a) 
    #print(arr2) 

    shuffle(a)
    print(a)
