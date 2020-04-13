# Mergesort:
# Best: nlogn
# Average: nlogn
# Worst: nlogn
# Space complexity worst: n

import unittest

def mergesort(arr): 
    if len(arr)>1:
        m = len(arr)//2

        left_arr = arr[:m]
        right_arr = arr[m:]

        mergesort(left_arr)
        mergesort(right_arr)

        # now we merge the sorted arrays left and right
        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1

        # at this point we have put all elements either of left or right
        # we have to complete until all elements are in the array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

class Testmergesort(unittest.TestCase):

    def test_1(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        mergesort(arr)
        self.assertEqual(arr, [2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_2(self):
        arr = [1]
        mergesort(arr)
        self.assertEqual(arr, [1])

    def test_3(self):
        arr = []
        mergesort(arr)
        self.assertEqual(arr, [])

    def test_4(self):
        arr = [1, 2]
        mergesort(arr)
        self.assertEqual(arr, [1, 2])


# driver code to test the above code 
if __name__ == '__main__': 
    unittest.main()
