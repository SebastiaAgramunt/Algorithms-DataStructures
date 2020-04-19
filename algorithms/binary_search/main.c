#include <stdio.h>
#include <stdlib.h>
#include "binary_search.h"
#include "quicksort.h"

int main(void){

	//int size = 7;
	//int array[] = {10, 9, 20, 5, 3, 13, 7};

	int size = 7;
	int val = 5;
	int *arr = (int*)malloc(size*sizeof(int));

	arr[0] = 10;
	arr[1] = 9;
	arr[2] = 20;
	arr[3] = 5;
	arr[4] = 3;
	arr[5] = 13;
	arr[6] = 7;
    
    printf("Array: \n"); 
    printArray(arr, size);

    int i = binary_search(arr, 0, size-1, val); 

    printf("Sorted array: \n"); 
    printArray(arr, size);

    printf("value %d is on index i %d\n",val ,i); 
    
	return 0;
}