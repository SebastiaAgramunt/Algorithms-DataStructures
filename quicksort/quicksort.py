from random import randint

def partition(arr, low, high):
	'''Puts all elements of arr smaller than arr[high-1]
	to the left and all the larger to the right of the array
	'''
	pivot = arr[high]
	i = low -1 #Begins at 0

	for j in range(low, high):
		if arr[j] < pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]

	return i+1

def quicksort(arr, low, high):
	if low < high:

		part = partition(arr, low, high)
		quicksort(arr, low, part-1)
		quicksort(arr, part+1, high)





if __name__ == '__main__':

	# Testing array
	to_sort = [10, 5, 3, 20, 4, 50]

	quicksort(to_sort,0, len(to_sort)-1)
	print(to_sort)

	# Tesitng random array
	to_sort = [randint(0,100) for i in range(200)]
	print("array to sort:\n{}".format(to_sort))

	quicksort(to_sort, 0, len(to_sort)-1)
	print("sorted array:\n{}".format(to_sort))

