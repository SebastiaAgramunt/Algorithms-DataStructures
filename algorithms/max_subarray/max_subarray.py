import sys

def MaxCrossing(arr, l, r, m):
    left_sum = -sys.maxsize
    right_sum = -sys.maxsize

    cum_sum = 0
    for i in range(m, l-1, -1):
        cum_sum += arr[i]
        if cum_sum>left_sum:
            left_sum = cum_sum

    cum_sum = 0
    for i in range(m+1, r+1):
        cum_sum += arr[i]
        if cum_sum>right_sum:
            right_sum = cum_sum

    return left_sum+right_sum

def MaxSubarray(arr, l, r):

    if l==r:
        return arr[l]

    m = (l+r)//2

    return max(MaxSubarray(arr, l, m), 
        MaxSubarray(arr, m+1, r), 
        MaxCrossing(arr, l, r, m))


if __name__ == "__main__":

    arr = [1, -13, 5, -8, 5, -3, 10]
    n = len(arr)
    print(MaxSubarray(arr, 0, n-1))
    #print(MaxCrossing(arr, 0, len(arr)-1, 3))