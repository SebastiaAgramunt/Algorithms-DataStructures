#include <stdlib.h>
#include <stdio.h>
#include "quicksort.h"

void swap(int* a, int* b){
	int a_val = *a;

	*a = *b;
	*b = a_val;
}

void printArray(int* arr, int size)  
{  
    int i;  
    for (i = 0; i < size; i++){
    	printf("%d ", arr[i]);
    }  
    printf("\n");
}

int partition(int* arr, int low, int high){
	int i = low-1; //starting at -1
	int pivot = arr[high]; //starting at lenght -1 (last element)

	for(int j=low; j<=high-1; j++){
		if(arr[j] < pivot){
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i+1], &arr[high]);
	return(i+1);
}

void quicksort(int* arr, int low, int high){
	if(low < high){
		int mid = partition(arr, low, high);

		quicksort(arr, low, mid-1);
		quicksort(arr, mid+1, high);

	}
}
