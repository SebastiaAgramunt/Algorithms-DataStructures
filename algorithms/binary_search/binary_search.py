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


def binary_search(arr, low, high, val):
	
	if high >= low:

		i = low + (high-low)//2

		if arr[i] == val:
			return i
		if arr[i] > val:
			return binary_search(arr, low, i-1, val)
		else:
			return binary_search(arr, i+1, high, val)
	else:
		return None


if __name__ == '__main__':

	# Tesitng random array
	to_sort = [randint(0,100) for i in range(50)]
	quicksort(to_sort, 0, len(to_sort)-1)
	print("Sorted array:\n{}".format(to_sort))

	val = 10
	s = binary_search(to_sort,0 ,len(to_sort)-1, val)

	if s is not None:
		print("Found element {} on index {}".format(val,s))



