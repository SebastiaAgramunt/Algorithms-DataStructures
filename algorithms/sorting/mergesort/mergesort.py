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

    def test_1_bis(self):
        arr = [7, 10, 90, 38, 95, 98, 85, 17, 54, 60, 75, 23, 89, 73, 9, 54,
         61, 72, 51, 79, 71, 95, 58, 84, 37, 81, 78, 60, 77, 32, 29, 48, 36,
         67, 16, 21, 11, 76, 73, 86, 92, 17, 29, 14, 30, 29, 71, 23, 63, 22,
         82, 49, 48, 23, 96, 56, 95, 56, 89, 77, 90, 87, 40, 85, 92, 63, 71,
         21, 58, 41, 19, 57, 18, 25, 93, 51, 15, 24, 16, 8, 81, 71, 23, 53,
         76, 21, 1, 67, 52, 6, 79, 50, 96, 1, 36, 70, 5, 14, 68, 52, 92, 69,
         72, 20, 84, 2, 18, 21, 45, 22, 88, 6, 21, 65, 46, 47, 11, 99, 31, 93,
         40, 33, 37, 40, 2, 98, 7, 39, 56, 76, 80, 79, 45, 99, 87, 27, 30, 54,
         51, 39, 45, 22, 77, 66, 6, 57, 61, 88, 76, 1, 58, 37, 34, 64, 22, 75,
         35, 50, 76, 16, 30, 48, 54, 95, 80, 29, 98, 55, 46, 9, 82, 91, 2, 71,
         19, 16, 78, 100, 90, 32, 9, 54, 69, 36, 94, 22, 67, 31, 37, 44, 77,
         45, 20, 27, 2, 96, 99, 25, 58, 14]

        mergesort(arr)

        sol = [1, 1, 1, 2, 2, 2, 2, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9, 10, 11, 11,
         14, 14, 14, 15, 16, 16, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21,
         21, 21, 21, 21, 22, 22, 22, 22, 22, 23, 23, 23, 23, 24, 25, 25, 27,
         27, 29, 29, 29, 29, 30, 30, 30, 31, 31, 32, 32, 33, 34, 35, 36, 36,
         36, 37, 37, 37, 37, 38, 39, 39, 40, 40, 40, 41, 44, 45, 45, 45, 45,
         46, 46, 47, 48, 48, 48, 49, 50, 50, 51, 51, 51, 52, 52, 53, 54, 54,
         54, 54, 54, 55, 56, 56, 56, 57, 57, 58, 58, 58, 58, 60, 60, 61, 61,
         63, 63, 64, 65, 66, 67, 67, 67, 68, 69, 69, 70, 71, 71, 71, 71, 71,
         72, 72, 73, 73, 75, 75, 76, 76, 76, 76, 76, 77, 77, 77, 77, 78, 78,
         79, 79, 79, 80, 80, 81, 81, 82, 82, 84, 84, 85, 85, 86, 87, 87, 88,
         88, 89, 89, 90, 90, 90, 91, 92, 92, 92, 93, 93, 94, 95, 95, 95, 95,
         96, 96, 96, 98, 98, 98, 99, 99, 99, 100]

        self.assertEqual(arr, sol)

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
