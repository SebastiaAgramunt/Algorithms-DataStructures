# Given a array of numbers representing the stock prices of a company in 
# chronological order, write a function that calculates the maximum profit you could have 
# made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, 
# since you could buy the stock at 5 dollars and sell it at 10 dollars.


########################################################################################
# Algorithm: remember we need to buy before selling we can do this in one loop keep track
# of the maximum profit found so far and the minimum sale price. Always check if
# the max profit 

from typing import List
from sys import maxsize

def maxprofit(prices_history: List[int]) -> int:
    min_price = maxsize
    max_profit = 0
    for price in prices_history:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit



if __name__ == "__main__":
    arr = [9, 11, 8, 5, 7, 10]
    #arr = [5, 8, 3, 9, 0, 0, 1]
    print(f"max profit for array:\n{arr}\nis {maxprofit(arr)}")
